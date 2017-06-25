EmpDataDict = {'name':'harman','age':24,'city':'santa clara'}

print EmpDataDict['city']

EmpDataDict['phone'] = 987654321
 
print EmpDataDict
EmpDataDict['city'] = 'Long beach'
print EmpDataDict

print '-' * 50

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    'NY': 'City in New York',
    'OR': 'City in Oregon'
}

print "california has: ", cities[states['California']] 

print '-' * 50

for state, abr in states.items():
    print "{} has abbreviation {}".format(state, abr)

print '-' * 50

for state, abr in states.items():
    print "{} has city: {}".format(state, cities[abr])
    
states['Arizona'] = 'AZ'
states['Washington'] = 'WT'

#Note that there is no city corresponding to the new states added
#to avoid erroring out use get() with default value

print '-' * 50
for state, abr in states.items():
    print "City for {}: {}".format(state, cities.get(abr, 'Does not Exist'))

