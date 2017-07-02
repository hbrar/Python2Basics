def print_two(*args):
    arg1, arg2 =  args
    print "arg1: %s, arg2: %s" % (arg1, arg2)
    
print_two("harmn", "brar")
#be very cautious about the indentation
#if you indent above print, it will not print
#everything indented after the function def is part of the function

from sys import argv

def print_argv(x):
    script, arg1, arg2 =  x
    print "arg1: %s, arg2: %s" % (arg1, arg2)
    
print_argv(argv)

def print_sum(a, b):
    print a+b
    
print_sum(3,4)

def return_sum(c,d):
    return c + d
    
print return_sum(4,6)
