# First small adaptivity test
# We test if a python list of GridFunctions with autoupdate=True
# is updated correctly when the grid is refined.
from ngsolve import Mesh, H1, GridFunction, dx, grad, \
        BilinearForm, LinearForm, Preconditioner, CGSolver, \
        Draw
from netgen.occ import unit_square

# Create a mesh
mesh = Mesh(unit_square.GenerateMesh(maxh=0.4))

# Define a finite element space
fes = H1(mesh, order=3, dirichlet="left|bottom|right|top", autoupdate=True)

# Define bilinear and linear forms
u, v = fes.TnT()

a = BilinearForm(fes)
a += grad(u)*grad(v)*dx

f = LinearForm(fes)
f += 1*v*dx

# Set up a preconditioner
c = Preconditioner(a, type="multigrid", inverse="sparsecholesky")

# Define GridFunctions
gf_u1 = GridFunction(fes, autoupdate=True)
gf_u2 = GridFunction(fes, autoupdate=True)

# Append GridFunctions to a python list
gfs = [gf_u1, gf_u2]

# Solve the system
a.Assemble()
f.Assemble()
inv = CGSolver(a.mat, c.mat)

# Solve the system for each GridFunction in the list
for gf in gfs:
    gf.vec.data = inv * f.vec

# Visualize the solution, pause for 1 second
Draw(gfs[0], mesh, "u1")
Draw(gfs[1], mesh, "u2")
input("Press any key to continue...")

# Refine the mesh
mesh.Refine()

# Check if the GridFunctions are updated
Draw(gfs[0], mesh, "u1-updated")
Draw(gfs[1], mesh, "u2-updated")
input("Press any key to continue...")

# Solve the system
a.Assemble()
f.Assemble()
inv = CGSolver(a.mat, c.mat)

# Solve the system for each GridFunction in the list
for gf in gfs:
    gf.vec.data = inv * f.vec

# Visualize the solution, pause for 1 second
Draw(gfs[0], mesh, "u1")
Draw(gfs[1], mesh, "u2")
input("Press any key to continue, and exit...")
