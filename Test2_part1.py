# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:07:18 2022

@author: Juan Orduna 
"""

# Test 2 - Computational Take Home, Part 1

import numpy as np

# Reading in Files

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
