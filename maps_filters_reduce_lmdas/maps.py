list_1  = [1,-2,-3,-4,-8,-7,0]
# maps

# def absoulte(num):
#     return abs(num)

# abs_list_1 = list(map(absoulte,list_1))
# print(abs_list_1)

# abs_list_1 = list(map( lambda num: abs(num),list_1))
# print(abs_list_1)

# filters

def even_no_filter(num):
    return num%2 == 0

only_even_list = list(filter( even_no_filter, list_1))
print(only_even_list)

only_even_list = list(filter( lambda num: num%2 == 0, list_1))
print(only_even_list)
