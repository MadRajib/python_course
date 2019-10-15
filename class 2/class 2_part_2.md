
# Strings

- are Immutable
- type name is __str__



```python
type("ghf")
```




    str




```python
# eg.
a = "hrllo"
a[0] = 'h'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-31-6b53d118cedb> in <module>
          1 # eg.
          2 a = "hrllo"
    ----> 3 a[0] = 'h'
    

    TypeError: 'str' object does not support item assignment



```python
# eg.
type("string")
```




    str



#### To convert other types to string use __str()__:


```python
# eg.
    str(45)
```




    '45'




```python
str(7.00002)
```




    '7.00002'



#### To define string use matching single quotes (')  or double quotes (").


```python
# eg.
    x = "node js"
    y = 'electron js'
```

__Note:__
> python has no __char__ type

- To create character we use single length strings


```python
# eg.
a = 'a' # "a"
```


```python
a
```




    'a'



#### To get the value of a character use __ord()__ function


```python
# eg.

    print('a :',ord('a'),end="")
    print(' z :',ord('z'))
    
    print('A :',ord('A'),end="")
    print(' Z :',ord('Z'))
```

    a : 97 z : 122
    A : 65 Z : 90


## String Indexing 

- Strings can be refered as an array.

- Python is zero indexed array , like c/c++/java e.i the element count starts from 0 onwards!


```python
# eg.
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabets[0]
    
```




    'a'




```python
alphabets[5]
```




    'f'



#### Negative Indexing

   H&nbsp; |&ensp; E &ensp;|&ensp; L &ensp;|&ensp; L &ensp;|&ensp; O &ensp;|&ensp; W &ensp;|&ensp; O |&ensp; R &ensp;|&ensp; L &ensp;|&ensp; D &ensp;|
<br>
<br>
 0&ensp; &emsp;1&ensp; &emsp;2&ensp; &emsp;3&ensp; &emsp;&ensp;4&ensp; &emsp;5&ensp; &emsp;&ensp;6&ensp; &emsp;7&ensp; &emsp;8&ensp; &emsp;9
<br>
<br>
 -10&ensp; -9&ensp; &ensp;-8&ensp; &ensp;-7&ensp; &ensp;&ensp;&nbsp;-6&ensp; &ensp;&nbsp;-5&ensp; &ensp;&nbsp;-4&ensp; &ensp;&nbsp;-3&ensp; &ensp;&nbsp;-2&ensp; &ensp;&nbsp;-1 


```python
# eg.
temp = "HELLOWORLD" 
print(temp[-1])
```

    D



```python
print(temp[-6])
```

    O



```python
print(temp[-10])
```

    H


### String Slicing

string [ start, end ] ,excluding end!
<br>
<br>
Mathematically: string [ start, end )


```python
temp = "HELLOWORLD"
```


```python
# eg
print(temp[0:5]) # HELLO

print(temp[1:]) # ELLOWORLD

print(temp[:]) # HELLOWORDLD

print(temp[2:7]) # LLOWO

print(temp[:-3]) # HELLOWO

print(temp[-3:]) # RLD

# if we wrap round we get empty string
print(temp[-3:2]) # empty string
```

    HELLO
    ELLOWORLD
    HELLOWORLD
    LLOWO
    HELLOWO
    RLD
    


### String Concatanation

Strings can be manipulated through a veriety of operators:
<br>
<br>
- __'+'__ : To concatanate:


```python
# eg.
"kilo" + "meter"
```




    'kilometer'



__Note:__
> Other data types cannot be directly concatanated with string objects.
<br>
<br>
> They have to converted to string object using __str()__


```python
# eg
"kilo" + 56
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-76-96ebde621c3e> in <module>
          1 # eg
    ----> 2 "kilo" + 56
    

    TypeError: must be str, not int



```python
"kilo" + str(56)
```




    'kilo56'



__Note:__
> For any index n :
<br>
> S[:n] + S[n:] == S
<br>
> Also works with negative numbers and out of bounds


```python
temp[:4] + temp[4:]
```




    'HELLOWORLD'




```python
temp[:-6] + temp[-6:]
```




    'HELLOWORLD'




```python
temp[:20] + temp[20:]
```




    'HELLOWORLD'



- __* (Multiplication)__ : To Concatanate Strings more number of times


```python
# eg.
"hie_" * 10
```




    'hie_hie_hie_hie_hie_hie_hie_hie_hie_hie_'



- __- (Subtraction), / (division), ** (exponant)__: Does work with strings
<br>
- __% (Modulo)__ : works as a formating machanism.

### String Literals

- any two string literals that are nex to each other are stuck together automatically!


```python
# eg.
"hie" "bie"
```




    'hiebie'



- Newlines are ignored between parentheses. Long strings can be built up over multiple
lines:


```python
# get
quote = ("Where is will"
        "There is a smith")
quote
```




    'Where is willThere is a smith'



- If a single- or double-quote character itself needs to be in the string,
<br>
use the other kind of quote to define the string at the outermost level.


```python
# eg.
print("'Hie' he said to her.")
print('"Hmmm" he got in reply.')
```

    'Hie' he said to her.
    "Hmmm" he got in reply.


- use __\__ to escape a special character to include it


```python
# eg.
print("Bones said, \"He\'s dead, Jim.\"")
```

    Bones said, "He's dead, Jim."


- Some of the mostly used escape characters
> \\  &emsp; ->&emsp; Backslash<br>
> \n &emsp;->&emsp; Newline<br>
> \r  &emsp;->&emsp; carraige return<br>
> \t  &emsp;->&emsp; tab

- String literals can also be prefixed with certain single characters that change how the<br>
string is interpreted

    r          r"escape!\n"           Raw string: all backslashes are escaped automatically. In the
                                      example, the \n is a \ and an &emsp;n, not a newline.
                                                 
    b          b"this bytes"          Byte array: rather than becoming a string type, the value in
                                      quotes is interpreted as a raw series of bytes.
                                                 
    u          u"René Descartes"      Unicode string: the string is explicitly interpreted as a Unicode
                                      type.


```python
print(r"gf\thello world")
```

    gf\thello world


- Python has support for multiline strings, which preserve the newlines that are
inside of them.<br>
To create these, surround the text with either triple single quotes<br>
(''') or triple double quotes (""").


```python
# eg.
print("""This is line 1
this is line 2
this is line 3
so on and so fort""")
```

    This is line 1
    this is line 2
    this is line 3
    so on and so fort


### String Methods

1.__s.lower() , s.upper()__ : Returns __Lower__ or __Upper__ version of string.


```python
# eg.
a ="string methods"
print(a.lower())
print(a.upper())
```

    string methods
    STRING METHODS


2.__s.strip()__ : Returns a string with white space removed from start and end.


```python
# eg.
a = "     whitespaces    "
a.strip()
```




    'whitespaces'



3.__s.split(sep=None,maxsplit = -1)__ : Returns a list(array) of substrings by the given delimiter.(default: whitespace)


```python
# eg.
a = "abc def ghi jkl"
a.split()
```




    ['abc', 'def', 'ghi', 'jkl']




```python
a = "abc,def,ghi,jkl"
a.split(',')
```




    ['abc', 'def', 'ghi', 'jkl']




```python
a = "abc def ghi jkl"
a.split(" ", 1)
```




    ['abc', 'def ghi jkl']



4. __str.title()__: Returns title cased version of words


```python
b = "madhab sharma"
b.title()
```




    'Madhab Sharma'



5. __str.find('other')__ : Returns first index where 'other' occurs else returns -1


```python
a = "abc aaf ahiaa akl"
a.find('a')
```




    0




```python
a.find('aa')
```




    4




6.__str.rfind('other')__: Returns the highest index of 'other' in the string else -1


```python
a.rfind("a")
```




    14



7. __str.index('other')__: Same as find , but raises ValueError when not found


```python
a.index('ak')
```




    14




```python
a.index('lk')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-122-223e47a1746b> in <module>
    ----> 1 a.index('lk')
    

    ValueError: substring not found


8. __str.rindex('other')__: same as rfind, but raises value error 


```python
a.rindex('a')

```




    14




```python
a.rindex('z')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-124-c31956abd7f9> in <module>
    ----> 1 a.rindex('z')
    

    ValueError: substring not found


8.__str.rsplit(sep=None,maxsplit =-1)__: Same as split but from right


```python
a = "abc def ghi"
a.rsplit(maxsplit=1)
```




    ['abc def', 'ghi']



9.__str.rstrip([chars])__: removing trailing characters.
<br>
The chars argument is not a suffix ; rather all combination of its values are stripped.


```python
'mississippi'.rstrip('ipz')
```




    'mississ'



10.__str.splitlines(keepends=False)__: returns a list of lines in the string, breaking at line boundary.
> Line breaks are not include in the result list unlsess __keepends = True__


```python
a = ''' line 1
line 2
line 3
line 4
'''
a.splitlines()
```




    [' line 1', 'line 2', 'line 3', 'line 4']




```python
a.splitlines(keepends=True)
```




    [' line 1\n', 'line 2\n', 'line 3\n', 'line 4\n']



11.__str.replace('old','new')__: returns a string where old are changed to new.


```python
print(a.replace('line','para'))
```

     para 1
    para 2
    para 3
    para 4
    


12.__sep.join(list)__: opposite of split.


```python
'---'.join(['abc','def','ijkl'])
```




    'abc---def---ijkl'



13. __str.isalpha() str.isdigit() str.isspace() str.numeric()__ : Returns true if all characters in str are<br>

aplhabets, digit, whitespace or numeric(integers, fractions, subscript, superscript, roman numerals etc.(all written in unicode))


```python
"ab230nj#".isalpha()
```




    False




```python
"abasbbs".isalpha()

```




    True




```python
'10142'.isdigit()
```




    True




```python
'10124.0'.isdigit()
```




    False




```python
"adahdh79!@".isnumeric()
```




    False




```python
"45545".isnumeric()
```




    True




```python
'\u00BD'.isnumeric()
```




    True




```python
"{} {}".format("hi","bye")
```




    'hi bye'




```python
"{1} {0}".format("hi","bye")
```




    'bye hi'




```python
"{:>10}".format("Exam")
```




    '      Exam'




```python
"{:10}".format("Exam")
```




    'Exam      '




```python
"{:_>10}".format("Exam")
```




    '______Exam'




```python
"{:#<10}".format("Exam")
```




    'Exam######'




```python
"{1} {0:_>10}".format("hi","bye")
```




    'bye ________hi'




```python
"{:^10}".format("Exam")
```




    '   Exam   '




```python
"{:.4}".format("Examination")
```




    'Exam'




```python
"{:10.4}".format("Examination")
```




    'Exam      '




```python
"{:^10.4}".format("Examination")
```




    '   Exam   '




```python
'{:d}'.format(45)
```




    '45'




```python
'{:10d}'.format(45)
```




    '        45'




```python
'{:f}'.format(3.14592653)
```




    '3.145927'




```python
'{:.4f}'.format(3.14592653)
```




    '3.1459'




```python
'{:010.4f}'.format(3.14592653)
```




    '00003.1459'




```python
'{:+d}'.format(454)
```




    '+454'




```python
'{:f}'.format(-3.14592653)
```




    '-3.145927'




```python
'{:=4d}'.format(-45)
```




    '- 45'




```python
'{:=+04d}'.format(45)
```




    '+045'




```python
'{hello} {first}'.format(first= 'hi',hello="gelo")
```




    'gelo hi'




```python
person ={
    'first':'will',
    'second':'smith'
}
"{p[first]} {p[second]}".format(p=person)
```




    'will smith'




```python

```
