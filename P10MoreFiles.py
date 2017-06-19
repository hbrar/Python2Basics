from os.path import exists

inFileName = raw_input("Enter the file name you wish to copy from:")
inFileContent = open(inFileName).read()

outFileName =  raw_input("Enter the file name you want to copy to:")
print "Checking if the file with provided 'filename' exists....%r" % exists(outFileName)
open(outFileName,'w').write(inFileContent)
print "Copied!"

##Method 2
# inFileName = raw_input("Enter the file name you wish to copy from:")
# outFileName =  raw_input("Enter the file name you want to copy to:")
# open(outFileName,'w').write(open(inFileName).read())

## **NOTE close function only works on file object
##  **which is returned by open() BE CAREFUL
##  **INFILE = OPEN(INFILENAME)
##  **INFILE.CLOSE() WILL WORK FINE
##  ** but inFileName.close() will error out