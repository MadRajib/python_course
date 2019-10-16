# def square_number(num_list):
#     result = []
#     for i in num_list:
#         result.append(i**2)
#     return result

# my_number = square_number([1,2,3,4,5])
# print(my_number)


def square_number(num_list):
    # result = []
    for i in num_list:
        # result.append(i**2)
        yield i**2
    # return result

my_number = square_number([1,2,3,4,5])
# print(next(my_number))
# print(next(my_number))
# print(next(my_number))
# print(next(my_number))
# print(next(my_number))

# print(next(my_number))

def func():
    yield 1
    yield 2
    yield 3

print(next(func))
print(next(func))
print(next(func))
# for i in func():
#     print(i)