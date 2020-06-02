# USING PYTHON FOR AUTOMATION

# How to read files

# # Here we open "inputFile.txt" and configure it for reading. f is an object of type open()
# f = open('inputFile.txt','r')
# # here we print file content
# print(f.read())
# #closing the file
# f.close()

#------------------------------------------------------------------------------------------------
#another way for do the same task is printing row by row in a for loop.

# Here we open "inputFile.txt" and configure it for reading. f is an object of type open()
# f = open('inputFile.txt','r')

# count = 0

# here we print file content by rows in a for loop
# for row in f:
# 	print(str(count) + row)
# 	count = count + 1

# #closing the file
# f.close()

#------------------------------------------------------------------------------------------------

# # first, we open inputFile.txt for reading in f
# f = open('inputFile.txt','r')

# # here we go through f with a for loop and print only those lines that contains a "P" that indicates that studens pass the exams
# for row in f:
# 	row_split = row.split()		# split() method returns a list of strings after breaking the given string by the specified separator

# 	if row_split[2] == 'P':
# 		print(row)

# #closing the file
# f.close()

#---------------------------------------------------------------------------------------------
# writing files in Python

# first, we open inputFile.txt
# f = open('inputFile.txt','r')

# # then, we create passFile.txt for writing those students that have passed the exams
# passFile = open('passFile.txt','w')
# # Here we create failFile.txt for store those students that have failed the exams
# failFile = open('failFile.txt','w')

# # here we go through f with a for loop and print only those lines that contains a "P" that indicates that studens pass the exams
# for row in f:
# 	row_split = row.split()		# split() method returns a list of strings after breaking the given string by the specified separator

# 	if row_split[2] == 'P':
# 		passFile.write(row)		# here we write on passFile.txt those lines that contains a "P"

# 	if row_split[2] == 'F':
# 		failFile.write(row)

# #closing the inputFile
# f.close()
# # after operation, we close passFile.txt
# passFile.close()
# after store information on it, we close failFile.txt
# failFile.close()

#----------------------------------------------------------------------------------------------

import os
import shutil # this module allow us to move, copy, rename or delete files or folders from our file system

# the following instruction store in "directorio_actual" the current work directory
directorio_actual = os.getcwd()

# creates a folder named "python_codes"
# os.makedirs('python_codes')
# this instruction will return True or False, depending whether the directory exists or not in the location where we are
print(os.path.isdir('python_codes'))
# Returns the size of the file between single quotes
print(os.path.getsize('inputFile.txt'))
# returns list with all files and directories from the location where we are
print(os.listdir())
# returns list with all files and directories from the path 
print(os.listdir('C:\\wamp'))
# the following sentence copies a file from the directory where we are to another place indicated by a path
# shutil.copy('passFile.txt','C:\\Users\Bangho 5\Desktop\Zorro\Programación')
# moves a file from the directory where we are to another indicated location: shutil.move('file','location')
# shutil.move('passFile.txt','python_codes')

# the following instruction removes a file from the indicated location
# os.unlike('python_codes\\file')

os.rmdir('borrar')

