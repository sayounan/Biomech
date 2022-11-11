# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:07:18 2022

@author: Jessica Green, Juan Orduña, Sari Younan
"""

# Change this line for your computer
locPath = r"/Users/sayounan/Documents/University/2022 2-Fall/Biomechanics Intro (BIOE 3020)/Coding Assignment"


def read(path):  # Part 1
    import os
    import numpy as np

    filenames = os.listdir(path)
    filepaths = [os.path.join(path, name) for name in filenames]

    d = {}
    for _ in filepaths:
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


def Node(Mesh):  # Part 2-1

    refMat = {}
    defMat = {}

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
                                    if "Bas" in EN[0]:
                                        refMat.update({f'{EN[0]} Elem {k} Node {l}': [x, y, z]})
                                    elif "Adv" in EN[0]:
                                        refMat.update({f'{EN[0]} Elem {k} Node {l}': [x, y, z]})
                                elif "Def" in EN[0]:
                                    if "Bas" in EN[0]:
                                        defMat.update({f'{EN[0]} Elem {k} Node {l}': [x, y, z]})
                                    elif "Adv" in EN[0]:
                                        defMat.update({f'{EN[0]} Elem {k} Node {l}': [x, y, z]})
                    else:
                        continue
                else:
                    continue
        else:
            continue

    return refMat, defMat


outData = Node(dataIn)


def Strain_Math(Reference, Deformed):  # Part 2-2 & 3

    import numpy as np

    strai = {}
    # if '2D' in list(Reference.keys()):  # Part 2-2
    for i in range(0, len(Reference), 3):
        x1ref = list(Reference.values())[i][0]
        y1ref = list(Reference.values())[i][1]

        x2ref = list(Reference.values())[i+1][0]
        y2ref = list(Reference.values())[i+1][1]

        x3ref = list(Reference.values())[i+2][0]
        y3ref = list(Reference.values())[i+2][1]

        x1def = list(Deformed.values())[i][0]
        y1def = list(Deformed.values())[i][1]

        x2def = list(Deformed.values())[i+1][0]
        y2def = list(Deformed.values())[i+1][1]

        x3def = list(Deformed.values())[i+2][0]
        y3def = list(Deformed.values())[i+2][1]

        y23 = y2ref - y3ref
        y31 = y3ref - y1ref
        y12 = y1ref - y2ref

        x32 = x3ref - x2ref
        x13 = x1ref - x3ref
        x21 = x2ref - x1ref

        ux1 = x1def - x1ref
        uy1 = y1def - y1ref

        ux2 = x2def - x2ref
        uy2 = y2def - y2ref

        ux3 = x3def - x3ref
        uy3 = y3def - y3ref

        refMat = [[y23, 0.0, y31, 0.0, y12, 0.0], [0.0, x32, 0.0, x13, 0.0, x21], [x32, y23, x13, y31, x21, y12]]
        UMat = [[ux1], [uy1], [ux2], [uy2], [ux3], [uy3]]

        dotProd = np.dot(refMat, UMat)
        A2 = (x2ref * y3ref - x3ref * y2ref) + (x3ref * y1ref - x1ref * y3ref) + (x1ref * y2ref - x2ref * y1ref)
        stra = dotProd*1/A2

        EVN = list(Reference.keys())[i].split(' ')
        strai.update({f'{EVN[0]} {EVN[1]} {EVN[2]}': stra})

    return strai


strain = Strain_Math(outData[0], outData[1])

"""
    elif '3D' in list(Reference.keys()):  # Part 3
        for j in range(0, len(Reference), 3):
            x1ref = list(Reference.values())[j][0]
            y1ref = list(Reference.values())[j][1]
            z1ref = list(Reference.values())[j][2]

            x2ref = list(Reference.values())[j + 1][0]
            y2ref = list(Reference.values())[j + 1][1]
            z2ref = list(Reference.values())[j + 1][2]

            x3ref = list(Reference.values())[j + 2][0]
            y3ref = list(Reference.values())[j + 2][1]
            z3ref = list(Reference.values())[j + 2][2]

            x1def = list(Deformed.values())[j][0]
            y1def = list(Deformed.values())[j][1]
            z1def = list(Deformed.values())[j][2]

            x2def = list(Deformed.values())[j + 1][0]
            y2def = list(Deformed.values())[j + 1][1]
            z2def = list(Deformed.values())[j + 1][2]

            x3def = list(Deformed.values())[j + 2][0]
            y3def = list(Deformed.values())[j + 2][1]
            z3def = list(Deformed.values())[j + 2][2]

            y23 = y2ref - y3ref
            y31 = y3ref - y1ref
            y12 = y1ref - y2ref

            x32 = x3ref - x2ref
            x13 = x1ref - x3ref
            x21 = x2ref - x1ref

            ux1 = x1def - x1ref
            uy1 = y1def - y1ref

            ux2 = x2def - x2ref
            uy2 = y2def - y2ref

            ux3 = x3def - x3ref
            uy3 = y3def - y3ref
            
            
"""

for va in range(len(strain)):
    print(list(strain.keys())[va], f'strain:',  '\n', list(strain.values())[va], '\n')
