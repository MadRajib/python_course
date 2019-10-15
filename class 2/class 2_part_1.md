
# Difference between == and is

An `is` expression evaluates to True if two 
variables point to the same<br>
(identical) object.

An `==` expression evaluates to True if the objects
referred to by the variables are equal<br>
(have the same contents).

Example:


```python
a = [1,4,6,5]
c = [1,4,6,7]

b = a
```

__Does a and c has same content ?__


```python
a == c  
```




    False



__Does a and b has same content ?__


```python
a == b 
```




    True



__Does b and c has same content ?__


```python
b == c 
```




    False



__Does a and c are same object?__


```python
a is c 
```




    False



__Does a and b are same object ?__


```python
a is b 
```




    True



True since a and b are pointing to same objects

__Does b and c are same object ?__


```python
b is c 
```




    False



### What if we change the content of b ?


```python
a = [1, 4, 6, 5]
c = [1, 4, 6, 7]
b = a

b[2] = 5
b
```




    [1, 4, 5, 5]



__Does a and b have same content ?__


```python
a == b
```




    True



True because a and b are pointing to same object changing b means changing a .


```python
a
```




    [1, 4, 5, 5]



__Does a and b are same object ?__


```python
a is b 
```




    True



__Also :__ If we print the id() of a,b and c 
we find that a and b have same id() value!


```python
print(id(a))
print(id(b))
print(id(c))
```

    140482741908616
    140482741908616
    140482741908744

