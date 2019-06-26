def multiply(a,b):
    """ 
    multiply multiples para a and b.
    """
    return a*b


a =  int(input())
b = int(input())

print(multiply(a,b))

# Keyword argument passing
def key_function(a=1,b=2,c=3):
    print("a: ",a,"b: ",b,"c: ",c)

key_function()

key_function(4)
key_function(4,5)
key_function(4,5,6)
key_function(7,8,9,7)
key_function(a = 7,b =8,c =9)

key_function(b = 8,c =9,a =7)

# Positional-Keyword argument passing
def pos_key_function(a,b,c=3):
    print("a: ",a,"b: ",b,"c: ",c)

pos_key_function()
pos_key_function(1,2)
pos_key_function(1,2,5)

# prpblematic example
def myappend(x,lyst =[]):
    lyst.append(x)
    print(lyst)


# solution to above
def myappend(x,lyst =None):
    if lyst is None:
        lyst = []
    lyst.append(x)
    print(lyst)

myappend(6)
myappend(42)
myappend(12,[1,2])


# variable positional arguments
def var_pos_function(*args):
    for elem in args:
        print(elem," " ,end="")
    print()

var_pos_function()
var_pos_function(2)
var_pos_function(1,23,"hello")

# variable keyword arguments
def var_key_function(**args):
    print(args)
    for key,value in args.items():
        print("key ",key,"value :",value,end="")
    print()

var_key_function()
var_key_function(a= 2)
var_key_function(a=1,b=23,c ="hello")
 

























