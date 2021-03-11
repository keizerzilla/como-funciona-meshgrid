"""
curvaturas_principais.py
Artur Rodrigues Rocha Neto
artur.rodrigues26@gmail.com
"""

import numpy as np
import pandas as pd
import open3d as o3d

def load_xyz(filename):
    """
    Carrega nuvem em formato XYZ (arquivo CSV separado por espaço em branco).
    
    Parâmetros
        filename: caminho para a nuvem XYZ
    Retorno
        ans: matriz numpy de dimensão Nx3
    """
    
    ans = np.array(pd.read_csv(filename, sep=" "))
    return ans

def show_pointcloud(cloud):
    """
    Mostra uma nuvem de pontos em janela interativa.
    
    Parâmetros
        cloud: matriz numpy de dimensão Nx3
    Retorno
        Nada
    """
    
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(cloud)
    o3d.visualization.draw_geometries([pcd])

if __name__ == "__main__":
    bunny = load_xyz("bunny.xyz")
    print(f"Dimensão da nuvem: {bunny.shape}")
    