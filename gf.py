# Basic example for clarification of the usage of (auto)update
# for GridFunction, after a refinement of the mesh in NGSolve.

from ngsolve import *
from netgen.occ import unit_square

mesh = Mesh(unit_square.GenerateMesh(maxh=0.4))
fes = H1(mesh, order=1, autoupdate=True)

gf_u1 = GridFunction(fes, autoupdate=True)
gf_u1.Set(cos(x))

print("gf_u1.vec.FV().NumPy():\n", gf_u1.vec.FV().NumPy())
mesh.Refine()
print("gf_u1.vec.FV().NumPy():\n", gf_u1.vec.FV().NumPy())
