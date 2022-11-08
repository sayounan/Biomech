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


def Strain(Mesh):

    Refy = []
    Refx = []

    for i in range(len(Mesh)):
        if "Nodes" in list(Mesh.keys())[i]:
            if "Reference" in list(Mesh.keys())[i]:
                for j in range(len(list(Mesh.values())[i])):
                    y = list(Mesh.values())[i][j][1]
                    x = list(Mesh.values())[i][j][0]
                    Refx.append(x)
                    Refy.append(y)
    print(Refy)
    print(Refx)

"""
    for i in range(len(Mesh)):
        if "Nodes" in list(Mesh.keys())[i]:
            if "Reference" in list(Mesh.keys())[i]:
                y23 = list(Mesh.values())[i][1][1] - list(Mesh.values())[i][2][1]
                y31 = list(Mesh.values())[i][2][1] - list(Mesh.values())[i][0][1]
                y21 = list(Mesh.values())[i][1][1] - list(Mesh.values())[i][0][1]
                x32 = list(Mesh.values())[i][2][0] - list(Mesh.values())[i][1][0]
                x13 = list(Mesh.values())[i][0][0] - list(Mesh.values())[i][2][0]
                x21 = list(Mesh.values())[i][1][0] - list(Mesh.values())[i][0][0]
                # refnodes.append(list(Mesh.keys())[i])
                # refnodes.append(y23)
                # refnodes.append(y31)
                # refnodes.append(y21)
                # refnodes.append(x32)
                # refnodes.append(x13)
                # refnodes.append(x21)
                return y23, y31, y21, x32, x13, x21

            elif "Def" in list(Mesh.keys())[i]:
"""


Strain(dataIn)
