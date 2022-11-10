# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:07:18 2022

@author: Jessica Green, Juan Orduña, Sari Younan
"""

# Change this line for your computer
locPath = r"/Users/sayounan/Documents/University/2022 2-Fall/Biomechanics Intro (BIOE 3020)/Coding Assignment1"


def read(path):  # This is for reading data

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

print(f'First variable/matrix in dictionary: \n{list(dataIn.keys())[2]}\n{list(dataIn.values())[2]}\n')
print(f'Second line in second matrix in dictionary: {list(dataIn.values())[2][3]}\n')
print(f'Second value in second line in second matrix in dictionary: {list(dataIn.values())[2][3][1]}\n')

"""
def math(refMat, defMat):
    
    import numpy as np

"""


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
    cr = 0
    cd = 0

    for m in range(len(Mesh.keys())):
        if "Elems" in list(Mesh.keys())[m]:
            if "Ref" in list(Mesh.keys())[m]:
                if "Bas" in list(Mesh.keys())[m]:
                    for n in range(7):
                        d[f'{list(Mesh.keys())[m]} Elem {n}'] = re[n]
                elif "Adv" in list(Mesh.keys())[m]:
                    for o in range(404):
                        d[f'{list(Mesh.keys())[m]} Elem {o}'] = re[o]
            elif "Def" in list(Mesh.keys())[m]:
                if "Bas" in list(Mesh.keys())[m]:
                    for p in range(7):
                        d[f'{list(Mesh.keys())[m]} Elem {p}'] = de[p]
                elif "Adv" in list(Mesh.keys())[m]:
                    for q in range(404):
                        d[f'{list(Mesh.keys())[m]} Elem {q}'] = de[q]
        else:
            continue

    return re, de, d


outData = Node(dataIn)

print('f')
