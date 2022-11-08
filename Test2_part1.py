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
    nodes = []

    for i in range(len(Mesh)):
        if "Nodes" in list(Mesh.keys())[i]:
            if "Reference" in list(Mesh.keys())[i]:
                y23 = list(Mesh.values())[i][1][1] - list(Mesh.values())[i][2][1]
                y31 = list(Mesh.values())[i][2][1] - list(Mesh.values())[i][0][1]
                y21 = list(Mesh.values())[i][1][1] - list(Mesh.values())[i][0][1]
                x32 = list(Mesh.values())[i][2][0] - list(Mesh.values())[i][1][0]
                x13 = list(Mesh.values())[i][0][0] - list(Mesh.values())[i][2][0]
                x21 = list(Mesh.values())[i][1][0] - list(Mesh.values())[i][0][0]
                nodes.append(list(Mesh.keys())[i])
                nodes.append(y23)
                nodes.append(y31)
                nodes.append(y21)
                nodes.append(x32)
                nodes.append(x13)
                nodes.append(x21)

    print(nodes)


Strain(dataIn)
