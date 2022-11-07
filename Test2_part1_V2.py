# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:07:18 2022

@author: Jessica Green, Juan Orduña, Sari Younan
"""

# Change this line for your computer
locPath = r"C:\Users\hepbo\OneDrive\Documents\New UCA Fall 2022\Python Fall 2022\Test 2 part 1"


def read(local_path):  # This is for reading data

    import os
    import numpy as np

    folderpath = local_path
    filenames = os.listdir(folderpath)
    filepaths = [os.path.join(folderpath, name) for name in filenames]

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
    return d


dataIn = read(locPath)

"""
print(f'Second variable/matrix in dictionary: \n{list(dataIn.values())[1]}\n')
print(f'Second line in second matrix in dictionary: {list(dataIn.values())[1][1]}\n')
print(f'Fifth value in second line in second matrix in dictionary: {list(dataIn.values())[1][1][4]}\n')

print(f'Basic 2D Reference (Nodes): \n{list(dataIn.values())[11]}\n')


To "index" the dictionary use list(dataIn.values())[#], also the order of
indexing goes [item in dictionary][row][column]
"""

#Testing Loop to get the nodes only 
Nodes11 = []
for i in range(len(list(dataIn.values())[11])):
    Nodes11.append(list(dataIn.values())[11][i][3:6])


for i in range(len(dataIn.values())):
    for j in range(len(list(dataIn.values())[i])):
        Nodes11.append(list(dataIn.values())[i][j][3:6])
    
    
    
    
    
    
    