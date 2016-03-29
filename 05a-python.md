# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both sequences of values (of any type) that are indexed by intergers. However, tuples are immutable, meaning they can not be edited. The documentation also notes that tuples are heterogeneous while lists are homogeneous so while the functional values of a list are all equivalent, the functional values of a tuple can be different. The best explanation of this I saw was in a tuple representing the date where depending on the structure of the list a value can refer to month, date, year, hour, etc. This, I believe, helps to explain why tuples work as keys in dictionaries while lists do not. There needs to be a functional diference between the key and the value. Finally, tuples are hashable, while lists are not. Hash values are intergers produced from the information in the key object that determines a "bucket" for the pair to be placed in. This makes searching in a dictionary more efficient because you do not need to iterate through an entire list. This is especially useful when dealing with large datasets.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are unordered lists with no duplicate entries that behave like a collection of dictionary keys with no values. They behave like a dictionary because they contain only hashable items. Given a large set or list, it is faster to search a set because hash values break a set into buckets that can help direct the search. A list must be searched by iterating through the whole list. </br></br>
You would use a list when your collection needs to be ordered, contain duplicates, or both (say a visitor record where you want to be able to see who arrived first and who has visited multiple times). A set is more appropriate if order and duplicates are unimportant, particularly when the collection is large. This could be used for a visitor record when you just want a list of unique visitors. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is a construct that allows you to create an unnamed function, used to write clean, succinct code when you need a function but only need to use it once. </br>

>> When sorting lambda is useful to specify the value to sort by in a complex object. Ex: </br>
birthday_tuples = [
        (1989, 1, 5),
        (1988, 8, 20),
        (1955, 4, 18),
        (1956, 11, 30),
]
print (sorted(birthday_tuples, key=lambda birthday: birthday[1]))   # sort by month


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a way to apply a function to all (or a specific group of) elements in a list. While list comprehension is generally more efficient, concise, and easy to read than mapping they are also harder to debug because you can't print a statement inside of the loop. 

```
ratings = (10, 9, 5, 9, 7, 3, 2, 4)
'#list ratings out of 10'


def out_of_5(l):
    '#converts ratings to out of 5 via mapping'
    res = []
    for x in l:
        res.append(x/2)
    return (res)


def out_of_100(l):
    '#converts rating to out of 100 via list comprehension'
    return [x/2 for x in l]
 

def best(l):
    '#returns ratings above 5 via filtering'
    res = []
    for x in l:
        if x > 5:
            res.append(x)
    return res


def worst(l):
    '#returns ratings below 5 via list comprehension'
    return [x for x in l if x < 5]

zagats = {"billy's": 10, "sally's": 9, "bistro": 5, "cafe": 9}


def dic_out_of_5(l):
    '# returns dictionary restaurants names and rating out of 5'
    return {"name": x/2 for x in l}


 def best_of_set(l):
     '# creates set of ratings over 5 - this is a useless function'
     return  {x for x in l if x >5}
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

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

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





