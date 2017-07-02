def comp(a,b):
    if (a>b):
        print "{0} is greater than {1}".format(a,b)
    elif (b>a):
        print "{1} is greater than {0}".format(a,b)
    else:
        print "Both are equal"
        
comp(7,6)

#list
fruits = [1,'apple', 2, 'banana', 3, 'orange', 4, 'kiwi']

for fruit in fruits:
    print fruit
    
#Repeadting some task using range() function
nmbrs = []

for i in range(0,6):
    nmbrs.append(i)
    
print nmbrs

#while loop
j = 0
while j < 7: #cant initialize j like while j = 0 < 9
    print j
    j = j + 1
    
    