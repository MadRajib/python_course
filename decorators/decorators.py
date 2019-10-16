# def decorator_func(original_fun):

#     def wrapper_func():
#         print('wrapper executed this before {}'.format(original_fun.__name__))
#         return original_fun()
    
#     return wrapper_func


# def display():
#     print("display func ran")

# @decorator_func
# def display():
#     print("display func ran")

# display()

# decorated_display = decorator_func(display)
# decorated_display()


# def decorator_func(original_fun):

#     def wrapper_func(*args,**kwargs):
#         print('wrapper executed this before {}'.format(original_fun.__name__))
#         return original_fun(*args,**kwargs)
    
#     return wrapper_func



# @decorator_func
# def display():
#     print("display func ran")

# display()

# @decorator_func
# def display_info(name,age):
#     print('display_info ran with arguments ({},{})'.format(name,age))

# display_info('john',25)




# class decorator_class(object):

#     def __init__(self,original_fun):
#         self.original_fun =  original_fun

 
#     def __call__(self,*args,**kwargs):
#         print('wrapper executed this before {}'.format(self.original_fun.__name__))
#         return self.original_fun(*args, **kwargs)

# @decorator_class
# def display():
#     print("display func ran")

# display()

# @decorator_class
# def display_info(name,age):
#     print('display_info ran with arguments ({},{})'.format(name,age))

# display_info('john',25)



# def my_logger(original_fun):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(original_fun.__name__),level=logging.INFO)

#     def wrapper(*args,**kwargs):
#         logging.info(
#             'Ran with args: {},and kwargs: {}'.format(args,kwargs)
#         )
#         return original_fun(*args,**kwargs)
    
#     return wrapper

# def my_timer(original_fun):
#     import time

#     def wrapper(*args,**kwargs):
#         t1 = time.time()
#         result =  original_fun(*args,**kwargs)
#         t2 =  time.time() - t1
#         print('{} ran in: {} sec'.format(original_fun.__name__,t2))
        
#         return result

#     return wrapper

# @my_timer
# def display_info(name,age):
#     print('display_info ran with arguments ({},{})'.format(name,age))

# display_info('john',25)

from functools import wraps

def my_logger(original_fun):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_fun.__name__),level=logging.INFO)

    @wraps(original_fun)
    def wrapper(*args,**kwargs):
        logging.info(
            'Ran with args: {},and kwargs: {}'.format(args,kwargs)
        )
        return original_fun(*args,**kwargs)
    
    return wrapper

def my_timer(original_fun):
    import time

    @wraps(original_fun)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result =  original_fun(*args,**kwargs)
        t2 =  time.time() - t1
        print('{} ran in: {} sec'.format(original_fun.__name__,t2))
        
        return result

    return wrapper

@my_timer
@my_logger
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name,age))

display_info('john',25)