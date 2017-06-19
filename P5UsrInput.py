#Getting Input from user
print "What's your name?"
name = raw_input()
print "Where do you live?"
place = raw_input()
gender = raw_input("What is your gender?")
age = input("what is your age?")
print "{0:#>10} is a {3} years old {2} from {1}".format(name, place, gender, age)