sum = int(input("Type the sum\n"))
a = input("Enter the sequence seperated by space\n")
print(a)
a = [int(i) for i in a.split()]
d = dict()
found = False
for elem in a:
    if sum - elem in d:
        print(elem,sum-elem)
        found = True
        break
    d[elem] = 1
if found : 
    print("Yes")
else:
    print("No")