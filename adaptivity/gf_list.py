
from ngsolve import *
from netgen.occ import unit_square

# Create a mesh
mesh = Mesh(unit_square.GenerateMesh(maxh=0.4))

# Define a finite element space
fes = H1(mesh,
        order=3,
        #dirichlet="left|bottom|right|top",
        autoupdate=True)

# Define a grid function
gf_u1 = GridFunction(fes, autoupdate=True)
gf_u2 = GridFunction(fes, autoupdate=True)
gf_u3 = GridFunction(fes, autoupdate=False)
gf_u4 = GridFunction(fes, autoupdate=False)

# Append GridFunctions to a python list
# gfs = [gf_u1, gf_u2]

# Set coefficient functions
gf_u1.Set(x)
gf_u2.Set(y)
gf_u3.Set(x)
gf_u4.Set(y)

# Print NumPy arrays of the GridFunction data
print("gf_u1.vec.FV().NumPy():\n", gf_u1.vec.FV().NumPy())
print("gf_u2.vec.FV().NumPy():\n", gf_u2.vec.FV().NumPy())
print("gf_u3.vec.FV().NumPy():\n", gf_u3.vec.FV().NumPy())
print("gf_u4.vec.FV().NumPy():\n", gf_u4.vec.FV().NumPy())

# Refine the mesh
mesh.Refine()

# Update (some of) the grid functions
gf_u3.Update()
gf_u4.Update()

# Print NumPy arrays of the GridFunction data
print("after refinement:")
print("gf_u1.vec.FV().NumPy():\n", gf_u1.vec.FV().NumPy())
print("gf_u2.vec.FV().NumPy():\n", gf_u2.vec.FV().NumPy())
print("gf_u3.vec.FV().NumPy():\n", gf_u3.vec.FV().NumPy())
print("gf_u4.vec.FV().NumPy():\n", gf_u4.vec.FV().NumPy())
