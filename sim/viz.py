import pyvista as pv

import nbody_dev
import numpy as np

bodies = [nbody_dev.Body(1, np.random.rand(3,1)*50, np.zeros((3,1)), np.zeros((3,1)))  for _i in range(50)]

tree = nbody_dev.Node.build_octree(bodies)

pv.set_plot_theme("paraview")
p = pv.Plotter()

mesh = pv.PolyData([i.position for i in bodies])
p.add_mesh(mesh)

xrng = np.array([tree.min[0], tree.max[0]])
yrng = np.array([tree.min[1], tree.max[1]])
zrng = np.array([tree.min[2], tree.max[2]])
grid = pv.RectilinearGrid(xrng, yrng, zrng).outline()
p.add_mesh(grid, opacity=0.1)

def add_sub(p, i):
    xrng = np.array([i.min[0], i.max[0]])
    yrng = np.array([i.min[1], i.max[1]])
    zrng = np.array([i.min[2], i.max[2]])
    grid = pv.RectilinearGrid(xrng, yrng, zrng).outline()
    p.add_mesh(grid, opacity=0.1)    
    try:
        for j in i.get_children():
            add_sub(p, j)
    except:
        return
        
add_sub(p, tree)
p.show()
