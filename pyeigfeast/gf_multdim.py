# nested autoupdate for multdim gridfunctions
from ngsolve import Mesh, GridFunction, H1, cos, sin, x, y, Draw
from netgen.occ import unit_square

# Create mesh and finite element space
mesh = Mesh(unit_square.GenerateMesh(maxh=0.4))
fes = H1(mesh, order=0, autoupdate=True)

# Create gridfunction with two smooth components
gf = GridFunction(fes, multidim=2, autoupdate=True, nested=True)
gf.Set(cos(x), mdcomp=0)
gf.Set(sin(y), mdcomp=1)

# Print ndof, length of the gridfunctions, and the values of the components
print(f"coarse ndof = {fes.ndof}")
print(f"length of gf = ({len(gf.vecs[0])}, {len(gf.vecs[1])})")
print(f"values of components \ngf_1 = {gf.vecs[0]}"
      + f"\ngf_2 = {gf.vecs[1]}")

# Draw gridfunction
Draw(gf, mesh, "gf")

# Pause for visualization
input("Press any key to continue...")

# Refine mesh
mesh.Refine()

# Print ndof, length of the gridfunctions, and the values of the components
# for the refined mesh
print(f"refined ndof = {fes.ndof}")
print(f"length of gf = ({len(gf.vecs[0])}, {len(gf.vecs[1])})")
print(f"values of components \ngf_1 = {gf.vecs[0]}"
      + f"\ngf_2 = {gf.vecs[1]}")

# Draw gridfunction
Draw(gf, mesh, "gf")

# Pause for visualization
input("Press any key to continue and exit...")
