# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both values can be any type, and they are indexed by integers. But lists are mutable. Tuples are immutable
Lists cannot be keys because keys have to be hashable. Python hashes the key and stores it in the corresponding location (for the key-value pair). But when the key is modified and hashed again, then it would go to a different location. Then the system may be unable to find a key or there may be multiple entries for the same key. 


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both contain values, and supports the following format: "x in set”, “len(set)”, “for x in set”. But sets are immutable. Sets also do not support indexing, slicing, or other sequence-like behavior, but support mathematical operations like union, intersection, difference, and symmetric difference. Sets are unordered collection of unique elements, while lists are ordered/indiced and allow duplicates. To find an item in a set, set performs much quicker (especially with a large dataset) because a hash look up is used, so a look up for a value happens in a constant time. On the other hand, list has to go through the values in the list sequentially to find if the value exists.\n
>> Example of set:
```python
>> from sets import Set
>>
>> animal = set([‘bat’, ‘cat’, ‘chicken’, ‘dog’, ‘butterfly’, ‘whale’])
>> winged = set([‘bat’, ‘chicken’, ‘butterfly’])
>> mammal = set([‘bat’, ‘whale’, ‘dog’, ‘cat’])
>> bird = set([‘chicken’])
>> 
>> print winged & mammal #Returns: set([‘bat’])
>> print animal – mammal #Returns: set([‘chicken’,’butterfly’])
>> print ‘dog’ in winged #Returns: False
```
>> Example of using both list and set:
```python
#prints unique list of numbers in the list
num_list = [1,2,3,3,4,6,6,6]
for n in sorted(set(num_list)):
	print n
```

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is a shorthand to create anonymous functions, and the expression yields a function object. Unnamed object behaves like a function object. Expression “lambda arguments: expression” is equivalent to “def name(arguments):\n\treturn expression”. The following example sorts a list by the second index: sorted(given_list, key = lambda x: x[1])

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are constructs that allow sequences to be built from other sequences. They result in the same list of values, but the line of code is more readable using the list comprehensions.\n
>> Examples:\n
>> *List comprehension*\n
>> Print out evens from 0-5:
```python
numbers = range[5]
odd1 = map(lambda x: x, filter(lambda x: x%2==0, numbers))
odd2 = [x for x in numbers if x%2==0]
```
>> Print out cubes from 0-10 that are under 100:
```python
cube1 = map(lambda x: x**3, filter(lambda x: x**3<100, range[10]))
cube2 = [x**3 for x in range[10] if x**3<100]
```
>> *Dictionary comprehension*\n
>> Swap key and value:
```python 
{value:key for key, value in a_dict.items()}
```
>> *Set comprehension*\n
>> Print evens under 10 that are divisible by 3:
```python
x for x in range(1:10) if x%3==0 and x%2==0}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850


Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





