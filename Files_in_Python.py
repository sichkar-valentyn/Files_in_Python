# File: Files_in_Python.py
# Description: How to read informations from files in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. How to read informations from files in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Files_in_Python (date of access: XX.XX.XXXX)

# Working with files
inf = open('test.txt', 'r')  # Opening the file
s1 = inf.readline()
s2 = inf.readline()
inf.close()  # Closing the file

print(s1)
print(s2)

# Another way ho to open and close the file - it is recommended to use this way
with open('test.txt') as inf:
    s1 = inf.readline()
    s2 = inf.readline()

# Here file is alredy closed
print(s1)
print(s2)

# Useful function to eliminate simboles at the beginning and at the and while reading line from the file
with open('test.txt') as inf:
    s1 = inf.readline().strip()  # Now at the and it will not add the '\n'
    s2 = inf.readline().strip()
print(s1)
print(s2)

# Another ueful function to specify the way to the file in standard way for all OS
print()
import os  # Module we need in this case
p = os.path.join('.', 'dirname', 'filename.txt')  # First is folder, then subfolder and then filename
# The amount of folders can be any, at the end we type the name of the file
print(p)
print()
# For the Linux System it will show: './dirname/filename.txt'
# For the Windows System it will show: '.\dirname\filename.txt'

# Using loops
with open('test.txt') as inf:
    for line in inf:
        line = line.strip()
        print(line)

# Writing in the file
ouf = open('test1.txt', 'w')
ouf.write('Test text\n')  # Here we need to add '\n' to move to the next line
ouf.write(str(101))  # Here we need to use 'str()' to convert number to string
ouf.close()

# Another way to write in the file
with open('test1.txt', 'w') as ouf:
    ouf.write('Test text\n')
    ouf.write('str(202)')

# Checking if it is written in the file
# Pay attention that each new time we open file to 'w' it will delete everything it was before inside
print()
with open('test1.txt') as inf:
    for line in inf:
        line = line.strip()
        print(line)
