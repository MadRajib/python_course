list_1 = ['a','b','c','c']
list_2 = [1,2,3,4]

zip_list = list(zip(list_1,list_2))

print(zip_list)

xy, yz = zip(*zip_list)
print(xy)
print(yz)