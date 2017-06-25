filename = raw_input("Enter the filename >")

file = open(filename,'w')

#OPENING FILE IN WRITEMODE DOESN'T ALLOW YOU TO READ IT
#fileContent = file.read()
#print "Printing the file Content..."
#print fileContent

#Even without truncating, it truncates the file by default
#use append mode if you want to preserve original content.
print "Truncating the file..."
#file.truncate()
content = raw_input("Enter what you want to write to file:")
file.write(content)
file.close()