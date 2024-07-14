#data type - int,float, complex,bool,str -- these are fundamental data types in python
#fundamental datatype - text,numeric,boolean

"""Advance data types
Sequence types(List,tuple,range)
Mapping type(dict)
Set type(set,frozenset)
Binary type(bytes,bytesarray,memoryview) """

# 100 == 100
# true, false



#char datatype is not available - we use str datatype
#long datatype is available in on python 2 but not in python3-
#long can be defined using int(any bigger value can be represented by int)
#one type value to another value- type casting or coercing
#inbuilt python typecast functions - int(),float(),complex(),bool()
print(int(123.46))
#print(int(10+20j)) #you can't convert complex to int
print(float(23))
print(int(True))
print(int(False))
print(int("10"))
#print(int("10.4")) - value error-- string value must be base 10.
#print(int("0B11"))- value error-- string value must be base 10.
#we can covert anything to int except complex and string without base 10

#print(float(10+20j))-you can't convert complex to float
print(float("10.45"))#possible
#print(float("0B11"))- value error-- string value must be base 10.
#print(float(0B11))
#we can covert anything to float except complex

#complex number
#other types to complex - two forms
#form-1 : Complex(x)==> x+0j - real part
#form-2 : Complex(x,y)==> x+yj -- real part and imaginary
print(complex(10))
print(complex(True))
print(complex(10,2))
print(complex(10.2,2.4)) #x & y can be integer or float
#print(complex("10.5",2)) #if the first string is string second argument can't passed
#print(complex("10.5","2"))

#bool - other types to bool
print(bool(10))
print(bool(1))
print(bool(1))
print(bool(0))
print("Kedar question")
print(bool(0+0j))
print(bool(1+0j))
print(bool("")) #if the string empty False if not all other cases True
print(bool(' ')) #if the string empty False if not all other cases True --string is not empty
print(bool("0"))
print(bool("ten"))
#bool type never raise any error

#likewise string never raise any error - pass any value, it converts to string
print(str(10+9j))
print(str(1))

"If you want to specify the data type of a variable, this can be done with casting."
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#print("X="+str(x)+"Y="+y+"Z="+z) #can only concat string erro
print("X value is ",x)
print("Y value is ",y)
print("Z value is ",z)


