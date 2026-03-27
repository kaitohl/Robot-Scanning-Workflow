import slicer
import vtk
import numpy as np
import os

tip_node_name = "probetiptransform"
base_node_name = "ros2:tf2lookup:worldToworld"

# I added .txt to your path so it saves as a clean text file
save_path = "/home/robotics/Robot-Scanning-Workflow/Data/probetobase16.txt"

# 1. Grab the nodes
tip_node = slicer.util.getNode(tip_node_name)
base_node = slicer.util.getNode(base_node_name)

if tip_node and base_node:
    # 2. Calculate the math
    tip_to_base_vtk_matrix = vtk.vtkMatrix4x4()
    slicer.vtkMRMLTransformNode.GetMatrixTransformBetweenNodes(tip_node, base_node, tip_to_base_vtk_matrix)
    tip_to_base_numpy = slicer.util.arrayFromVTKMatrix(tip_to_base_vtk_matrix)
    
    # 3. Ensure the Data directory exists so the script doesn't crash on the first run
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # 4. Append the matrix to the file
    with open(save_path, "a") as f:
        np.savetxt(f, tip_to_base_numpy, delimiter=',', fmt='%.6f')
        
    print(f"Appended new pose to: {save_path}")
else:
    print(f"Error: Could not find '{tip_node_name}' or '{base_node_name}'.")