import numpy as np
import math
import vtk
from vtk.util.numpy_support import numpy_to_vtk
from vtk.util.numpy_support import vtk_to_numpy


def read_vtu(path):
    reader = vtk.vtkXMLUnstructuredGridReader()
    reader.SetFileName(path)
    reader.Update()
    return reader.GetOutput()


def write_vtu(path, mesh):
    writer = vtk.vtkXMLUnstructuredGridWriter()
    writer.SetInputData(mesh)
    writer.SetFileName(path)
    writer.Write()


in_vtu = "TemperatureField1D_ts_365_t_31536000.000000.vtu"
out_vtu = "TemperatureField1D_transport.vtu"

mesh = read_vtu(in_vtu)

T_vtk_array = mesh.GetPointData().GetArray("T")
T_numpy_array = vtk_to_numpy(T_vtk_array)
Dm = np.zeros((np.size(T_numpy_array), 1))

Dm_std = 2e-11  # standard diffusion coefficient @298 K [m2/s]
Ea = 17  # activation energy of bulk water [kJ/mol]
R_gas = 8.314e-3  # universal gas constant [kJ/K mol]

for i in range(0, np.size(Dm)):
    Dm[i] = Dm_std * math.exp((Ea / R_gas) * (1 / 298.15 - 1 / T_numpy_array[i]))

Dm_vtk = numpy_to_vtk(Dm)
Dm_vtk.SetName("Dm")

# add calc. T-dependent diffusion array
mesh.GetPointData().AddArray(Dm_vtk)
# remove unnecessary arrays
mesh.GetPointData().RemoveArray("T")
mesh.GetPointData().RemoveArray("p")
mesh.GetPointData().RemoveArray("darcy_velocity")

# use point to cell data filter
reader2 = vtk.vtkPointDataToCellData()
reader2.SetInputData(mesh)
reader2.Update()
mesh2 = reader2.GetOutput()

# update file
reader2.Update()
# get output
mesh2 = reader2.GetOutput()
# write output vtu
write_vtu(out_vtu, mesh2)

print("------------------------------------------------")
print("INFO: Output mesh written to: {}".format(out_vtu))
print("------------------------------------------------")
