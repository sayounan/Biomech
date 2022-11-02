# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:07:18 2022

@author: Juan Orduña
"""

# Test 2 - Computational Take Home, Part 1

import numpy as np

# Reading in Files

# The comment block below is to be removed, left there temporarily for reference.

"""
fName = ['Basic2D_Reference.ucd', 'Basic3D_Reference.ucd', 'Basic2D_Deformed.ucd', 'Basic3D_Deformed.ucd',
         'Adv2D_Reference.ucd', 'Adv3D_Reference.ucd', 'Adv2D_Deformed.ucd', 'Adv3D_Deformed.ucd']


def reading(Name):
    for i, name in enumerate(range(len(Name))):
        BA = Name[i].find('Basic')
        Deform = Name[i].find('Deformed')
        if BA == 1:
            Dim = Name[i].find('2D')
            if Dim == 1:
                BNodesR_2D = np.genfromtxt(Name, skip_footer=7, skip_header=1, delimiter=' ')
                BElemsR_2D = np.genfromtxt(Name, skip_header=9, delimiter=' ')
            else:
                BNodesR_3D = np.genfromtxt(Name, skip_footer=7, skip_header=1, delimiter=' ')
                BElemsR_3D = np.genfromtxt(Name, skip_header=9, delimiter=' ')
        else:
            Dim = Name[i].find('2D')
            if Dim == 1:
                ANodesR_2D = np.genfromtxt(Name, skip_footer=734, skip_header=1, delimiter=' ')
                AElemsR_2D = np.genfromtxt(Name, skip_header=405, delimiter=' ')
            else:
                ANodesR_3D = np.genfromtxt(Name, skip_footer=734, skip_header=1, delimiter=' ')
                AElemsR_3D = np.genfromtxt(Name, skip_header=405, delimiter=' ')
        if Deform == 1:
            Dim = Name[i].find('2D')
            if Dim == 1:
                BNodesD_2D = np.genfromtxt(Name, skip_footer=7, skip_header=1, delimiter=' ')
                BElemsD_2D = np.genfromtxt(Name, skip_header=9, delimiter=' ')
            else:
                BNodesD_3D = np.genfromtxt(Name, skip_footer=7, skip_header=1, delimiter=' ')
                BElemsD_3D = np.genfromtxt(Name, skip_header=9, delimiter=' ')
        else:
            Dim = Name[i].find('3D')
            if Dim == 1:
                ANodesD_2D = np.genfromtxt(Name, skip_footer=734, skip_header=1, delimiter=' ')
                AElemsD_2D = np.genfromtxt(Name, skip_header=405, delimiter=' ')
            else:
                ANodesD_3D = np.genfromtxt(Name, skip_footer=734, skip_header=1, delimiter=' ')
                AElemsD_3D = np.genfromtxt(Name, skip_header=405, delimiter=' ')

    return BNodesR_2D, BElemsR_2D, BNodesR_3D, BElemsR_3D, ANodesR_2D, AElemsR_2D, ANodesR_3D, AElemsR_3D, 
    BNodesD_2D, BElemsD_2D, BNodesD_3D, BElemsD_3D, ANodesD_2D, AElemsD_2D, ANodesD_3D, AElemsD_3D 


x = reading(fName)
"""


def read():
    import os
    folderpath = r"/Users/sayounan/Documents/University/2022 2-Fall/Biomechanics Intro (BIOE 3020)/Coding Assignment1"
    filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
    filenames = os.listdir(folderpath)

    d = {}
    for path in filepaths:
        for i in range(len(filenames)):
            if ".ucd" in filenames[i]:
                if "Basic" in filenames[i]:
                    d[f'{filenames[i]} Nodes'] = np.genfromtxt(filenames[i], skip_footer=7, skip_header=1,
                                                               delimiter=' ')
                    d[f'{filenames[i]} Elems'] = np.genfromtxt(filenames[i], skip_header=9, delimiter=' ')
                elif "Adv" in filenames[i]:
                    d[f'{filenames[i]} Nodes'] = np.genfromtxt(filenames[i], skip_footer=734, skip_header=1,
                                                               delimiter=' ')
                    d[f'{filenames[i]} Elems'] = np.genfromtxt(filenames[i], skip_header=405, delimiter=' ')
            else:
                continue

    for j in range(len(d)):
        print(list(d.keys())[j], f'\n')
        print(list(d.values())[j], f'\n')


read()

"""
# References
# Basic 2D
B2NodesR = np.genfromtxt('Basic2D_Reference.ucd', skip_footer=7, skip_header=1, delimiter=' ')
B2ElemsR = np.genfromtxt('Basic2D_Reference.ucd', skip_header=9, delimiter=' ')

# Basic 3D
B3NodesR = np.genfromtxt('Basic3D_Reference.ucd', skip_footer=7, skip_header=1, delimiter=' ')
B3ElemsR = np.genfromtxt('Basic3D_Reference.ucd', skip_header=9, delimiter=' ')

# Advanced 2D
A2NodesR = np.genfromtxt('Adv2D_Reference.ucd', skip_footer=734, skip_header=1, delimiter=' ')
A2ElemsR = np.genfromtxt('Adv2D_Reference.ucd', skip_header=405, delimiter=' ')

# Advanced 3D
A3NodesR = np.genfromtxt('Adv3D_Reference.ucd', skip_footer=734, skip_header=1, delimiter=' ')
A3ElemsR = np.genfromtxt('Adv3D_Reference.ucd', skip_header=405, delimiter=' ')

# ------------------------------------------------------------------------------

# Deformations
# Basic 2D
B2NodesD = np.genfromtxt('Basic2D_Deformed.ucd', skip_footer=7, skip_header=1, delimiter=' ')
B2ElemsD = np.genfromtxt('Basic2D_Deformed.ucd', skip_header=9, delimiter=' ')

# Basic 3D
B3NodesD = np.genfromtxt('Basic3D_Deformed.ucd', skip_footer=7, skip_header=1, delimiter=' ')
B3ElemsD = np.genfromtxt('Basic3D_Deformed.ucd', skip_header=9, delimiter=' ')

# Advanced 2D
A2NodesD = np.genfromtxt('Adv2D_Deformed.ucd', skip_footer=734, skip_header=1, delimiter=' ')
A2ElemsD = np.genfromtxt('Adv2D_Deformed.ucd', skip_header=405, delimiter=' ')

# Advanced 3D
A3NodesD = np.genfromtxt('Adv3D_Deformed.ucd', skip_footer=734, skip_header=1, delimiter=' ')
A3ElemsD = np.genfromtxt('Adv3D_Deformed.ucd', skip_header=405, delimiter=' ')
"""
