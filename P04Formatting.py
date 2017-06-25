#Formatting
#https://pyformat.info/

name  =  "Harman"
lname = "Brar"
print "My name is", name, ".I am from Earth."
print "My name is %s." % name, "I am from Earth."
print "My name is %s %s." % (name,lname), "I am from Earth."
print "My name is {} {}.".format(name,lname), "I am from Earth."
print "My name is {1} {0}.".format(name,lname), "I am from Earth."

#Padding
#old style
print "I am %10s" % name, "I am from Earth." #right aligned by default
print "I am %-10s" % name, "I am from Earth."

#New style, using format method
print "I am {:10}".format(name), "I am from Earth." # left aligned by default
print "I am {:<10}".format(name), "I am from Earth." 
print "I am {:>10}".format(name), "I am from Earth."
print "I am {:#<10}".format(name), "I am from Earth." #format method also has option to choose padding character
print "I am {:#>10}".format(name), "I am from Earth."
print "I am {:^10}".format(name), "I am from Earth."
print "I am {:#^10}".format(name), "I am from Earth."
print "I am {0:#^10}".format(name), "I am from Earth." #using index

#truncating 
#old style
print "I am %.5s" % name

#using format method
print "I am {:.5}".format(name)

#combining padding and truncating
print "I am %10.5s" % name
print "I am {:10.5}".format(name);

#padding numbers
print "{:d}".format(42)
print "{:10d}".format(42)
print "{:4.2f}".format(72.3274987237)

#parametrized formats
print "I am {:{padChar}{align}{width}}".format(name,width=10, padChar="#", align="^")

#more formatting
print "I am %r." % name  #Use the %r for debugging, since it displays the "raw" data of the variable
print "I am '%s'." % name

nameEval = "I am '%s'."
print nameEval % name

print name + lname #concatenates without space
print name, lname  #concatenates with space