#TEACHER CODE

import math #imports math module

#TODAYS CONCEPTS
#variable assignments

#example with string values
name = 'Joe Biden'
greeting = 'Hello ' + name + ". How are you doing today?"
#print(greeting)

#example with numerical values
x = math.pi
e = math.e
#print(int(x/e))

#functions
#parameters/arguments

#FUNCTION SYNTAX
#def functionName(parameters):
	#...do some stuff
    #return val (optional)

#declare and write greet function
def greet(name):
  return 'Hello ' + name + ". How are you doing today?"
  

greet('Ralu') #<-call greet function to greet Ralu

#declare and write divide function 
def divide(x, e):
	return x/e
#END OF TEACHER CODE

#MY CODE
#define bake function
def bake(pastry, shape):
	baking = "I baked a " + pastry + " that was shaped like a " + shape + "."
	return(baking)

#define subtract function
def subtract(num1, num2):
	result = num1-num2
	equation = "Evaluating equation " + str(num1) + "-" + str(num2) + "...\n" + str(num1) + "-" + str(num2) + "=" + str(result)
	return equation
#test and print examples of using functions
print(bake('cookie', 'star'))
print(bake('brownie', 'circle'))
print(bake('strudel', 'triangle'))
print(subtract(5,3))
print(subtract(2,6))
print(subtract(0.3,0.2))
#END OF MY CODE
