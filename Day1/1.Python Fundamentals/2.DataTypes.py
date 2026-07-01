### https://www.w3schools.com/python/python_datatypes.asp

# Text Type
text = "Hello, Python!"
print(text)
print(type(text))


### Numeric Types

# Integer
num = 10
print(num)
print(type(num))

# Float
decimal = 10.5
print(decimal)
print(type(decimal))

# Complex
complex_num = 3 + 4j
print(complex_num)
print(type(complex_num))


### Sequence Types

# List
my_list = [1, 2, 3]
print(my_list)
print(type(my_list))

# Tuple
my_tuple = (1, 2, 3)
print(my_tuple)
print(type(my_tuple))

# Range
my_range = range(5)
print(list(my_range))
print(type(my_range))


### Mapping Type
my_dict = {
    "name": "Sidra",
}
print(my_dict)
print(type(my_dict))


### Set Types

# Set
my_set = {1, 2, 3}
print(my_set)
print(type(my_set))

# Frozen Set
my_frozenset = frozenset({1, 2, 3})
print(my_frozenset)
print(type(my_frozenset))


### Boolean Type

flag = True
print(flag)
print(type(flag))


### Binary Types

# Bytes
my_bytes = b"Python"
print(my_bytes)
print(type(my_bytes))

# Bytearray
my_bytearray = bytearray(b"Python")
print(my_bytearray)
print(type(my_bytearray))

# Memoryview
my_memoryview = memoryview(my_bytes)
print(my_memoryview)
print(type(my_memoryview))


### None Type

nothing = None
print(nothing)
print(type(nothing))



############### output 
# (myvenv) PS D:\MLB-Internship\Day1\1.Python Fundamentals> python 2.DataTypes.py
# Hello, Python!
# <class 'str'>
# 10
# <class 'int'>
# 10.5
# <class 'float'>
# (3+4j)
# <class 'complex'>
# [1, 2, 3]
# <class 'list'>
# (1, 2, 3)
# <class 'tuple'>
# [0, 1, 2, 3, 4]
# <class 'range'>
# {'name': 'Sidra'}
# <class 'dict'>
# {1, 2, 3}
# <class 'set'>
# frozenset({1, 2, 3})
# <class 'frozenset'>
# True
# <class 'bool'>
# b'Python'
# <class 'bytes'>
# bytearray(b'Python')
# <class 'bytearray'>
# <memory at 0x0000029C918A4940>
# <class 'memoryview'>
# None
# <class 'NoneType'>