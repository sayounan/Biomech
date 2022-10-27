# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:07:18 2022

@author: Juan Orduna 
"""

#Test 2 - Computational Take Home, Part 1

import numpy as np
import pandas as pan

#Reading in Files"
data = np.genfromtxt('Basic2D_Reference.ucd', delimiter='\t', dtype=(None), skip_header=0)

data2 = pan.read_table('Basic2D_Reference.ucd')

n_nodes = data[0]
n_elems = data[1]

nodes = []
elems = []
"""
for i, row in enumerate(data):
    if i < n_nodes+1:
        # get nodes here
    else:
        # get connectivity here
"""