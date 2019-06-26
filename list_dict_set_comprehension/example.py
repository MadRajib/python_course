# get values from dictionaries
d = {1:5}
d[1]

# get(key, default_value) ,returns default value if key not found else returns
# the value associated with the key
print(d.get(1,0))

# Adding new key value pairs , is simple !
d[2] = 6

d[100] = 4

d["hjhhj"] = 6


# pop(key,default=None), del the key value pair and returns the value
d.pop(2)

# if key not found then default value is returned, here default is 0
print(d.pop(1,0))

# popitem() pops a random item from the dictionary
print(d.popitem())
print(d)


# del keyword is used delete a key: value pair
del d[1]

print(d)

# set comprehension

# here list comprehension is used to covert list to a set!
s = {x for x in [1,2,3,4,5]}

print(type(s))

# dictionaries comprehension
# here a dictionary is made where key is x and value is kye ^square.
dic =  { x:x**2 for x in [1,2,6,66]}

print(dic)
print(type(dic))

# dic comprehension with filter,

# save only those pairs in which key e.i divisble by 2
dic =  { x:x**2 for x in [1,2,3,66] if x%2==0 }

print(dic)
print(type(dic))

# list comprehension to slice dictionary using another dictionary
cord = { 'x':1,'y':2,'z':3,'r':1,'theta':2,'pi':3}

polar_key = {'r','theta','pi'}

print(cord.items())
print(cord.keys())
print(cord.values())

d = { key:value for key , value in cord.items() if key in polar_key } 

print(d)
