from sys import argv

#Below works fine but just for building 
#understanding do it using script variable 
#filename = argv[1]
script, filename = argv

#Open function returns a file object
file = open(filename)

print "Below is file %r's data:" % filename
#read function of the file object
print file.read()

print "Enter another filename you wish to read"
filename =  raw_input(">")

file = open(filename)

print "File %r's content:" % filename
print file.read()