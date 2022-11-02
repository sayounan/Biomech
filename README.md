# Biomech Test 2 Take Home

This code reads given reference and deformation meshes and uses finite element analysis to calculate strain based on the
changes from the reference to the deformation meshes of the corresponding structures.

First function follows a local path to ucd files location. Then creates a dictionary (variable "d"). The function then 
reads the names of individual files in the folder and checks for the substring ".ucd" in the file name. If found,
it checks for the substrings "Basic" & "Adv" in the file names. When it finds that, it follows the respective 
numpy.genfromtxt method specific to the file. It assigns it to a variable name according to the file name followed by 
what the matrix represents. Those variables are simultaneously appended to the predefined dictionary. Finally, the 
dictionary is returned to be used later. 

The following print statements are reference points for dictionary indexing methods.

