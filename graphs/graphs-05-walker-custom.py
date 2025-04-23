#r: networkx
#r: matplotlib

from typing import cast, Any
import networkx as nx # type: ignore
import matplotlib.pyplot as plt # type: ignore
import Rhino.Geometry as rg # type: ignore beaause using stubs
import ghpythonlib.treehelpers as th # type: ignore


import graph_helpers as graph 

# DECLARE INPUT VARIABLES OF PYTHON COMPONENT
m = cast(rg.Mesh, m)  # type: ignore
s = cast(int, s)  # type: ignore

G, dv,de = graph.DualGraphFromMesh(m)

all_points  = []
all_face_ind  = []


for i in range(m.Faces.Count):
    if nx.has_path(G, s, i):
        SP = graph.shortestPath(G, s, i)
        all_points.append(SP[0])
        all_face_ind.append(SP[1])
               
a= dv
b = de
c = d = th.list_to_tree(all_face_ind)



#plot
# path= r"C:\Users\david\Desktop\Session02\session02\images\MDPA_plot5.png"
# ghelp.PlotGraph(G, path)