from mymodule import divide
import sys

# mymodule.py: now prints out mymodule
# __main__ refers to the file that is bein RUN

print(divide(6, 2))


# sys.path shows where pyhton will look to find files to import
# will first look at first item in path
# if it's not there, it will look in the next level up
# first path is always path of the file you ran
# EXPORTPATH?

# show path
# print(sys.path)


# show all the module that have been imported
# python will check these modules to see if that import is there
# when we import a file, it runs through the file
# if you were to import the same thign many times, can run over and over withotu doing anyting
# keeps track of what has already been imported

print(sys.modules)
