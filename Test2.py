# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:07:18 2022

@author: Jessica Green, Juan Orduña, Sari Younan
"""

# Change this line for your computer
locPath = r"C:\Users\hepbo\OneDrive\Documents\New UCA Fall 2022\Python Fall 2022\Test 2 part 1"


def read(path):
    import os
    import numpy as np

    filenames = os.listdir(path)
    filepaths = [os.path.join(path, name) for name in filenames]

    d = {}
    for path in filepaths:
        for i in range(len(filenames)):
            if ".ucd" in filenames[i]:
                if "Basic" in filenames[i]:
                    d[f'{filenames[i]} Nodes'] = np.genfromtxt(filenames[i], skip_footer=7, skip_header=1,
                                                               delimiter=' ', usecols=(1, 2, 3))
                    d[f'{filenames[i]} Elems'] = np.genfromtxt(filenames[i], skip_header=9, delimiter=' ',
                                                               usecols=(3, 4, 5))
                elif "Adv" in filenames[i]:
                    d[f'{filenames[i]} Nodes'] = np.genfromtxt(filenames[i], skip_footer=734, skip_header=1,
                                                               delimiter=' ', usecols=(1, 2, 3))
                    d[f'{filenames[i]} Elems'] = np.genfromtxt(filenames[i], skip_header=405, delimiter=' ',
                                                               usecols=(3, 4, 5))
            else:
                continue
    return d


dataIn = read(locPath)


def Node(Mesh):
    import numpy as np

    refMat = []
    defMat = []

    for i in range(len(list(Mesh.keys()))):
        if "Elems" in list(Mesh.keys())[i]:
            for j in range(len(list(Mesh.keys()))):
                if "Nodes" in list(Mesh.keys())[j]:
                    EN = list(Mesh.keys())[i].split(".")
                    NN = list(Mesh.keys())[j].split(".")
                    if EN[0] == NN[0]:
                        EV = list(Mesh.values())[i]
                        NV = list(Mesh.values())[j]
                        for k in range(len(EV)):
                            for l in range(len(EV[k])):
                                ind = int(EV[k][l])
                                ind -= 1
                                x = NV[ind][0]
                                y = NV[ind][1]
                                z = NV[ind][2]
                            if "Ref" in EN[0]:
                                refMat.append([x, y, z])
                            elif "Def" in EN[0]:
                                defMat.append([x, y, z])
                    else:
                        continue
                else:
                    continue
        else:
            continue

    Reference = np.array(refMat)
    Deformation = np.array(defMat)

    re = np.split(Reference, 494)
    de = np.split(Deformation, 494)

    d = {}

    for m in range(len(Mesh.keys())):
        EN = list(Mesh.keys())[m].split(".")
        if "Elems" in list(Mesh.keys())[m]:
            if "Ref" in list(Mesh.keys())[m]:
                if "Bas" in list(Mesh.keys())[m]:
                    for n in range(7):
                        d[f'{EN[0]} Elem {n}'] = re[n]
                elif "Adv" in list(Mesh.keys())[m]:
                    for o in range(404):
                        d[f'{EN[0]} Elem {o}'] = re[o]
            elif "Def" in list(Mesh.keys())[m]:
                if "Bas" in list(Mesh.keys())[m]:
                    for p in range(7):
                        d[f'{EN[0]} Elem {p}'] = de[p]
                elif "Adv" in list(Mesh.keys())[m]:
                    for q in range(404):
                        d[f'{EN[0]} Elem {q}'] = de[q]
        else:
            continue

    return d


outData = Node(dataIn)

def Strain_Math(dictionary):
    
    import numpy as np
    for i in range(len(outData)):
        x1 = [i][0][0]
        y1 = [i][0][1]
        z1 = [i][0][2]
    
        x2 = [i][1][0]
        y2 = [i][1][1]
        z2 = [i][1][2]
    
        x3 = [i][2][0]
        y3 = [i][2][1]
        z3 = [i][2][2]
    

strain = Strain_Math(outData)

print('ertgh')