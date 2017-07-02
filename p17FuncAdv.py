# docstring
def Square(x, y):
    """I am Documentation String or docstring. I define what a function does """
    a, b = x * x, y * y
    print "Square {0} : {1}, Square {2} : {3}".format( x, a, y, b)

Square(2,3)

# Global variables cannot be directly assigned a value within a function 
g = 9

def readglobal():
    print "readglobal() => g: " + str(g)
    
readglobal()

def try_read_global_local():
    print g #results in error instead of printing global
    g = 11
    print g

#try_read_global_local()

x = "global" 
print "------------Global scope------------"
print "x : " + x
def modify_global_local():
    #Needed to modify global variable
    print "------------Local scope------------"
    x = "local"
    #global g
    print "x : " + x
    print "x : " + globals()['x']
    globals()['x'] = "Updated Global"
    print "x : " + x
    
modify_global_local()
print "------------Global scope------------"
print "x : " + x

#Aliases

def foo():
    return "Called"
    
print "calling foo:", foo()
f = foo
print "calling f:",f()
print "calling foo:", foo()

# a function without any return statement returns none
# to see none use print with function call

#default values are evaluated at the point of function definition in the scope

i = 5
def foobar(arg = i):
    print arg

i = 6
foobar()
#default value is evaluated only once
# In the following list is initialised as empty only once

def addToList(a, L = []):
    L.append(a)
    return L

print addToList(1)
print addToList(2)
print addToList(3)

b = []
print addToList(4, b)
print addToList(5, b)
print addToList(6, b)
print "original b: ", b

#call by value or reference
x = 5
print x

def callBy(arg):
    arg = 9
    print "x is passed neither as value or reference but as object reference/ call by sharing"

callBy(x)
print x

y = 5
print y

def callBy2(arg = None):
    arg = 9
    print "y is passed neither as value or reference but as object reference"

callBy2(y)
print y

z = []
print z

def callBy3(arg = None):
    arg.append(7)
    print "z is passed neither as value or reference but as object reference"

callBy3(z)
print z

# If you pass immutable arguments like integers, strings or tuples to a function, 
# the passing acts like call-by-value. The object reference is passed to the function parameters.
# They can't be changed within the function, because they can't be changed at all, i.e. they are immutable. 
# It's different, if we pass mutable arguments. They are also passed by object reference, but they can be changed 
# in place in the function. If we pass a list to a function, we have to consider two cases: Elements of a list can 
# be changed in place, i.e. the list will be changed even in the caller's scope. If a new list is assigned to the name,
# the old list will not be affected, i.e. the list in the caller's scope will remain untouched.  

#if you dont want default to be shared between subsequent calls, do as below
xy = []
def addToList2(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L

print addToList2(1)
print addToList2(2)
print addToList2(3)

#Keyword Arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "Action : ", action
    print "Voltage: ", voltage
    print "Type: ", type
    print "State: ", state
    print "-" * 50
    
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument

#keyword arguments must follow positional arguments
#their order is not important.
#No argument may receive a value more than once

# formalParameter vs *formalParameters vs **formalParametersList

def cheeseshop(argument, *argumentsList, **argumentsDictionary):
    print "Formal parameter 'Argument' contains ", argument
    print "-" * 50
    print "Formal parameter '*argumentsList' contains: "
    for arg in argumentsList:
        print arg
        
    print "-" * 50
    print "Formal parameter '**argumentsDictionary' contains: "
    keys = sorted(argumentsDictionary.keys())
    for k in keys:
        print k, ":", argumentsDictionary[k]

cheeseshop("Argument", "ListArgument1",
           "ListArgument2",
           shopkeeper='DictionaryArgument1',
           client="DictionaryArgument2",
           sketch="DictionaryArgument3")
        
# unpacking Argument list
# The reverse situation occurs when the arguments are 
# already in a list or tuple but need to be unpacked 

arglist = [3, 6]
print range(*arglist)

d = {"state": "CA", "voltage": "alot", "action": "Run"}
parrot(**d)

# LAMBDA EXPRESSIONS

def CreateMultiplyBy(n):
    return  lambda x: x * n

MultiplyBy2 = CreateMultiplyBy(2)
print MultiplyBy2
print MultiplyBy2(4)

MultiplyBy5 = CreateMultiplyBy(5)
print MultiplyBy5(4)