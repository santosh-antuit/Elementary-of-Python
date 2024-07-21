#Advanced data types
#bytes data type - group of byte numbers or values
x=[10,20,30,40]
b=bytes(x)
print(type(b))
print(b[0])
print(b[-1])
print(b[0:4]) #understand this 
print("check above")
for x in b: print(x)
#here byte() is constructor 
print("----------------------------------Byte - First Example")
#In the range 0 to 256 can be defined as bytes
#y=[10,20,256,258]
#by=bytes(y)
#bytes datatype is immutable, for example
z=[10,30,40,50]
bz=bytes(z)
print(b[0])
# b[0]=120  --error because which is immutable

#bytes array
#bytes array vs byte data type - only difference bytes array is mutable.
p=[100,200,30,40]
bp=bytearray(p)
print(bp[0])
bp[0]=110
print(bp[0])

#If our value requirement in these range then only use bytes and bytesarray.Generally we dont use these datatypes
#bytes and bytes array application - binary data(images or video files). Internally these will be binary but in python bytes.
#byte is not available in python.


#List datatype
#Lists are one of 4 built-in data types in Python used to store collections of data, 
#the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage
#To represent group of values as single object with Insertion order is preserved and duplicates are allowed
#list of values are represent in []
#hetegenous values are allowed
#it is growable(it can increased or reduced)
#how to remove item from list
l=[]
print(type(l))
l.append(1000)
l.append(2000)
l.append(4000)
l.append(4000)
print(l)
l.append('santosh')
print(l)
l.append(None)
print(l)
#apply indexes or slice
print(l[-1])
print(l[-1])
l.remove(l[-1])
print(l)
print(l[2:])

# * operator can be applied to any object
l1 =l*2
print("with *",l1)
#there is no limit for number of values in list - but having huge values are not recommended
#list functions
print(len(l))#5 
print(l.count(4000)) #2 number of occurance of item(value) in an list - value based
l1 = l.copy()
print("With Copy - ",l1)
l2 = ['Happy','Santosh']
l2.extend(l1)
print(l2)
print(l1)
# what is iterable in python (list,set,dict)
print(l1.index(4000)) #The index() method returns the position at the first occurrence of the specified value.
l1.insert(0,"FIrsttime") # takes two argument #value & position in which it has to insert
print(l1)
l1.pop(0) # only position or index
print(l1)
l1.remove("santosh") # if value is not in the list throws an error
print(l1)
l1.reverse()
print(l1)
l1.insert(0,500)
l1.sort()
print(l1)
l1.clear() #removes all elements from the list
print(len(l1))
print(l1)

#all list's methods have been covered above

#ordered - If you add new items to a list, the new items will be placed at the end of the list. However using insert,remove
#method ordered can be change in generall order of items will not change
#changable
#allow duplicates
#hetergenous
#another way to create a list is using list() constructor
newlist = list(("customer",'product')) # double parantesis
print(newlist)

#Accessing list
# l[0],l[-1], using for loop ,using slice
print("Accessing the list")
print(l)
print(l[2:5]) #from index position 2 to 5-1
print(l[2:10]) #from index position 2 to end of the list -higher value allowed - 
print(l[2:3]) #from index position 2 to end value -1 -- start index included and end index excluded
print(l[2:4]) #from index position 2 to end value -1
print(l[:2]) # alwways start from the index 0
print(l[:1]) # alwways start from the index 0
print(l[:0]) # alwways start from the indext - end values must be greater than 0
print(l[:]) # alwways start from the index 0 and end value will be len(l)
print(l[2:]) # leaving out end value goes till end of the list
print("Negative index")
print(l)
print(l[-1:]) #start value included
print(l[-1:-1]) #start value included ->Empty list -> start value greater than end value
print(l[-1:-3]) #start value included ->Empty list -> start value greater than end value
print(l[-3:-1]) #start value included -> end value greater than start val
print("Change the value of specific item")
print(l)
l[3]='Happy'
print(l)
l[1:3] =['Santy','Santa']
print(l)
#can also use -> insert(position,value)

