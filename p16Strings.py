#repeating strings, use *

print 3 * 'go' + 'Bro' 

#strings are indexed
# there  s no character type in python, a character is a string with length 1
word = 'HARMAN'
print word[0]
print word[-1]

#slicing a string
print word[0:2]             # characters from position 0 (included) to 2 (excluded)
# Note how the start is always included, and the end always excluded. 
# This makes sure that s[:i] + s[i:] is always equal to s:
# An omitted first index defaults to 0
# An omitted second index defaults to length of the string

print word[:2] + word[2:]  

print word[-2:]
print word[0:0] # prints nothing

#slicing gracefully handles indexoutof range error
#print word[24] # error
print word[:24]

#strings are immutable and cannot be changed
#word[0] = 'G' #error

#For length of a string, use built in function len()
print len(word)