# print("hello")
# 
# 

d = {1:5}
# d[1]
# print(d.get(1,0))

d[2] = 6

d[100] = 4

d["hjhhj"] = 6

# d.pop(2)

# print(d.pop(1,0))

# print(d.popitem())
# print(d)

# del d[1]

# print(d)

# set comprehension

# s = {x for x in [1,2,3,4,5]}

# print(type(s))

# dictionaries comprehension

# dic =  { x:x**2 for x in [1,2,6,66]}

# print(dic)
# print(type(dic))


# dic =  { x:x**2 for x in [1,2,3,66] if x%2==0 }

# print(dic)
# print(type(dic))


cord = { 'x':1,'y':2,'z':3,'r':1,'theta':2,'pi':3}

polar_key = {'r','theta','pi'}

print(cord.items())
print(cord.keys())
print(cord.values())

d = { key:value for key , value in cord.items() if key in polar_key } 

print(d)
