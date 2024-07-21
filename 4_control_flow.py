# control flow - > 
# program consists set of statements
# always start from the begining


#important point - immutable vs fundamental data types
#all fundamental data types are immutable(non-changable nature) - i.e once you create an object it can't be change.
#if you try to change the data type new object will be created.
#why immutable is needed for fundatamental data types -for example
#everything in python is object
x=10  #x is pointing to 10
x=11 #x is now pointing to 11 by creating new object instead of changing the old value
#memory wasted or performance slow ?
x=10
print(id(x))
xz=20
print(id(xz))
y=10
print(id(y))
z=20
print(id(z))
#here 10 object is being shared by x,y(only single object being created with 2 references) likewise 20 being shared by xz,z
#if any 10 is changed to 15 it gonna effect other reference hence python creates new object for new value.

#Everything in python is object
#All fundatamental datatypes(object) are immutable -list is mutable

#instead of memory address we can also "is" operator to check both are pointing to same ojects or not
#re-using of same objects -- for int numbers reusing is  possible only till 256(range 0-256) --commonly used range 0-256
#re-using of same objects -- for floating/complex numbers reusing is not possible -frequently used range is defined.
#immutable always helpful for string object -- commonly used string literals in program
#immutable always work for boolean objects -- python interpreter creates objects for bool and integer
#not for string literals. 
#then why float & complex are immuatable -really not required. At language level generalized level implemented. 
print(x is z)
print(x is y)
print(xz is z)

#Python is case sensitive
name ="santosh"
Name ="santosh1"
NAME ="santosh2"
a = "alde"
print(name)
print(a)
#name,Name and NAME are different variables 
#MultiWord Variables
#1. Camel case - First letter of all words are capital letter except first word - myVariableName
#2. Pascal case - First letter of all words are capital letter - MyVariableName
#3. Snake case - each word seperated by _(underscore)

#Assignment
#Assign multiple values 
x,y,z = 10,20,30
#One value with Multiple variable
a=b=c ="Orange"

#Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables.
#This is called unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Global variable and local variable 
x = "awesome" #Outside the function hence global variable

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#The global Keyword
def myfunc():
  global x #the variable belongs to the global scope
  x = "fantastic" 

myfunc()
#x = "Sa"
print("Python is " + x)