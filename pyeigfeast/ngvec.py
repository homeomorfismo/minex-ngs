# Testing pyeigfeast NGvecs
from ngsolve import Mesh, H1
from netgen.occ import unit_square
from pyeigfeast import NGvecs

mesh = Mesh(unit_square.GenerateMesh(maxh=0.4))
fes = H1(mesh, order=0, autoupdate=True)

# Create two random vectors
ngvecs = NGvecs(fes, 2)
ngvecs.setrandom(seed=1)


# Print the two random vectors before the refinement
print("ndof coarse fes:", fes.ndof)
print("ngvecs[0]:\n", ngvecs._mv[0].FV().NumPy())
print("Len(ngvecs[0]):\n", len(ngvecs._mv[0].FV().NumPy()))
print("ngvecs[1]:\n", ngvecs._mv[1].FV().NumPy())
print("Len(ngvecs[1]):\n", len(ngvecs._mv[1].FV().NumPy()))

# Pause for visualization
input("Press Enter to continue...")
# Refine the mesh
mesh.Refine()

# Print the two random vectors after the refinement
print("ndof refined fes:", fes.ndof)
print("ngvecs[0]:\n", ngvecs._mv[0].FV().NumPy())
print("Len(ngvecs[0]):\n", len(ngvecs._mv[0].FV().NumPy()))
print("ngvecs[1]:\n", ngvecs._mv[1].FV().NumPy())
print("Len(ngvecs[1]):\n", len(ngvecs._mv[1].FV().NumPy()))
