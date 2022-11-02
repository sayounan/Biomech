# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:07:18 2022

@author: Jessica Green, Juan Orduña, Sari Younan
"""

# Change this line for your computer
locPath = r"/Users/sayounan/Documents/University/2022 2-Fall/Biomechanics Intro (BIOE 3020)/Coding Assignment1"


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

    for j in range(len(d)):
        print(list(d.keys())[j], f'\n')
        print(list(d.values())[j], f'\n')

    return d


dataIn = read(locPath)
