
<img src="/vvaezian.github.io/Pic/Python-logo.png" alt="Logo" height="200">
<em>* Sources: <a href="https://courses.edx.org/courses/course-v1:MITx+6.00.1x_9+2T2016/info" target="_blank">this</a> online course, 
	<a href="https://www.amazon.com/Data-Science-Scratch-Principles-Python/dp/149190142X" target="_blank">this</a> book, and <a href="https://medium.freecodecamp.org/an-a-z-of-useful-python-tricks-b467524ee747"> this </a> post.</em><br>


### Strings "123"
String Methods<br>
```python
s = 'abcabc'
s.upper()
s.isupper()
s.capitalize()
s.index('b')
s.index('z')
s.find('b')
s.find('z')
s.count('c')
s = s.replace('b','z')
s = s.replace('b','z',1)
t = 'abc def ghi'
t.split(' ')
output = ''.join(i for i in list1)
```

```python
"ABCABC"
False
"Abc"
1
error
1
-1
2
"azcazc"
"azcabc"

['abc', 'def', 'ghi']


```<br>

While <kbd>index</kbd> works for both strings and lists, <kbd>find</kbd> works only with strings.<br>
	    
String Slicing<br>
```python
s = 'abcd'
s[0]
s[-1]
s[1:3]
s[::-1]
```
```python
a
d
bc
dcba
```<br>

Since strings are immutable, there is no method to replace an arbitrary character of a string 
(e.x. replacing the second 'o' in 'foo'). But we can use the following function
(taken from <a href="http://stackoverflow.com/a/9188460/2445273" target="_blank"> here </a>):<br>
<pre class = "prettyprint">
    def arbit_replace(s, i, c):
        return s[:i] + c + s[i + 1:]

    print arbit_replace('foo', 2, 'z')</pre>
```python
foz
```<br>
	    
<b>F-Strings</b> (Python 3.6+)<br>
<pre class=prettyprint>
name = 'John'
print(f"name is {name}.")

for x in range(3):
  print(f"{x/3:.3f}")  # print to precision of 3 digits

from datetime import datetime
date=datetime(2018, 1, 1)
print(f"Date is {date:%B %d, %Y}.")
</pre>
```python


name is John.


0.000
0.333
0.667

Date is January 01, 2018.
```<br>
</div>
</details>


### Lists [1, 2, 3]
```python

list1 = ['a', 'b', 'c']
list1.remove('b')
del list1[-1]
list1.append('z')
list1.insert(1,63)

```
```python

['a','c']
['a']
['a', 'z']
['a', 63, 'z']

```<br>

<b>Enueration</b><br>
<pre class="prettyprint">
for index, item in my_list:
    do_something(index, item)
</pre><br>
If we just want the indexes:<br>
<pre class="prettyprint">
for i in range(len(documents)):  # not Pythonic
    do_something(i) 
for i, _ in enumerate(documents):  # Pythonic
    do_something(i) 
</pre><br>

<b>List Comprehension</b>:<br>
<pre class="prettyprint">
list1 = [i for i in range(100) if i not in range(30, 50)]
list2 = [(x, y)
         for x in range(10)
         for y in range(10)]
list3 = [(x, y) 
         for x in range(10)
         for y in range(x + 1, 10)]
list4 = [0 for _ in range(5)]
</pre><br>
<br>
Concatenating lists:<br>
<pre class=prettyprint>
x = [1, 2]
x.extend([3, 4])  # x is [1, 2, 3, 4]</pre><br>
If you don't want to modify x use list addition:<br>
<pre class=prettyprint>
x = [1, 2]
y = x + [3, 4] # y is [1, 2, 3, 4]; x is unchanged</pre><br>
Appending to lists one item at a time:<br>
<pre class=prettyprint>
x = [1, 2]
x.append(0) # x is now [1, 2, 0]</pre>
</div>
</details>



### Tuples (1, 2, 3)
Tuples are lists' immutable cousins. Pretty much anything you can do to a list that doesn't involve modifying it, you can do to a tuple.<br>
```python

tuple1 = (3)
print tuple1
type(tuple1)
tup2 = (3,)
print tuple2
type(tuple2)

```
```python

3
&lt;type 'int'&gt;<br>
(3,)
&lt;type 'tuple'&gt;

```<br>
</div>
</details>


### Dictionaries {1:'a', 2:'b', 3:'c'}
```python

dic={'a':'cat', 'b':'bear', 'c':'cow'}
dic.keys()
dic.values()
dic['b']
'a' in dic
'cat' in dic
'cat' in dic.values()
del dic['b']
dic['d'] = 'dog'
dic['z']
dic.get('z')
dic.get('z', 'nothing')

```
```python


['a', 'b', 'c']
['cat, 'bear', 'cow']
'bear'
True
False
True
{'a':'cat', 'c':'cow'}
{'a':'cat', 'c':'cow', 'd':'dog'}
KeyError
None
nothing

```<br>
```python

for key, value in aDict.iteritems():
    print "letter: {} Animal: {}".format(key,value)
```<br>
```python

a = ''.join('{}{}'.format(key, str(val)) for key, val in dict1.items())
```<br>

<kbd>iteritems()</kbd> to <kbd>items()</kbd> is like <kbd>xrange</kbd> to <kbd>range</kbd>.<br>
<br>
Sort a dictionary by values: <br>
```python
sorted(myDict.items(), key=lambda item: item[1], reverse=True)

```<br>
	    
<b>defaultdict</b><br>
A defaultdict is like a regular dictionary, except that when you try to look up a key it doesn't contain, it first adds a value for it using a zero-argument function you provided when you created it.<br>

<pre class=prettyprint>
from collections import defaultdict

a = defaultdict(int)
b = defaultdict(str)
c = defaultdict(list)
d = defaultdict(tuple)
e = defaultdict(set)
f = defaultdict(dict)

g = defaultdict(lambda: [5, 8])
g[2][1] = 1

print(a[1])
print(b[1])
print(c[1])
print(d[1])
print(e[1])
print(f[1])
print(g[1])
print(g.items())</pre>
```python

0

[]
()
set([])
{}
[5, 8]
[(1, [5, 8]), (2, [5, 1])]

```<br>
<br>

<b>Counter</b><br>
<ul>
<li>A Counter turns a sequence of values into a defaultdict(int)-like object, mapping keys to counts.<br>
<pre class="prettyprint">
from collections import Counter
c = Counter([0, 1, 2, 0])   # c is (basically) { 0 : 2, 1 : 1, 2 : 1 }
</pre><br>
<li>A useful method of <samp>Counter</samp> is <samp>most_common</samp>.<br>
<pre class="prettyprint">
# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
    print word, count
</pre><br>
<li>Counting occurances of words/letters/symbols in a text given as a list (e.x. by myText.split()):<br>
First approach<br>
<pre class="prettyprint">
word_counts = {}
for word in document:
if word in word_counts:
    word_counts[word] += 1
else:
    word_counts[word] = 1
</pre><br>
Second approach:<br>
<pre class="prettyprint">
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1
</pre><br>
Third approach:<br>
<pre class="prettyprint">
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1
</pre><br>
Fourth approach:<br>
<pre class="prettyprint">
word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1
</pre><br>
Fifth approach:<br>
<pre class="prettyprint">
word_counts = Counter(document)
</pre><br>
</div>
</details>



### Sets {1, 2, 3}
Set is like list but repetition doesn't matter. {1,1,2} = {1,2}<br><br>
Adding two sets a and b: <samp>a.union(b)</samp> (for lists we can simply write <samp>a + b</samp><br>
** Checking membership in a set is faster compared to list. The same goes for deletting an element (<a href='https://stackoverflow.com/a/8929320/2445273'>source</a>)
</div>
</details>



### Array and Matrix
```python
a = [1] * 3

```
```python
[1, 1, 1]

```<br>
The following functions do the same thing (making a zero matrix of m by n)<br>
<pre class="prettyprint">
def matrix1(m,n):
    M = []
    for i in xrange(m):
        M.append([])
        for j in xrange(n):
            M[i].append(0)
    return M
    
def matrix2(m,n):
    M = []
    for i in xrange(m):
        M.append([0]*n)
    return M

def matrix3(m,n):
    return [[0] * (n) for i in xrange(m)]
</pre><br>
</div>
</details>



### Exceptions
<pre class="prettyprint">
def listDivision(l1,l2):
    '''Assumes: l1 and l2 are lists of same size
    Returns a list containing the meaningful
    values of l1[i]/l2[i]'''
    result=[]
    for n in range(len(l1)):
        try:
            result.append(l1[n]/float(l2[n]))
        except ZeroDivisionError, e:	# in Python 3.x we must write `except ZeroDivisionErroe as e:`
            result.append(float('NaN'))
            print e
        except: #For all other kinds of exceptions
            result.append('Bad Arg')
            print 'listDivision called with bad arg'
    return result</pre>
<code>
>>> listDivision([1,2,3],[4,5,6])<br>
<span style="color:blue">[0.25, 0.4, 0.5]</span><br>
>>> listDivision([1,2,3],[4,5,0])<br>
<span style="color:blue">float division by zero<br>
[0.25, 0.4, 'NaN']</span><br>
>>> listDivision([1,2,3],[4,5,'a'])<br>
<span style="color:blue">listDivision called with bad arg<br>
[0.25, 0.4, 'Bad Arg']</span>
</code><br>
</div>
</details>



### Classes
<pre class=prettyprint>
class Coordinate(object):
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0

c = Coordinate(3,4)
Origin = Coordinate(0,0)
</pre><br>
<img src="Pic/frame.png" alt="frame" height="300"><br>
```python
isinstance(c, Coordinate)

```
```python
True

```<br>
<pre class=prettyprint>
class Coordinate(object):
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    def xDifference(self,other):
        return (self.x - other.x)
</pre><br>
<ul>
<li>The <kbd>__init__()</kbd> method (AKA initialization method or class constructor) is called immediately after an instance of the class is created.</br>
<li>In all class methods, <kbd>self</kbd> refers to the instance whose method was called. But in the specific case of the <kbd>__init__()</kbd> method, the instance whose method was called is also the newly created object.
<li>Python interpreter translates <kbd>obj1 &lt obj2</kbd> into a method call on <kbd>obj1</kbd> (namely <kbd>obj1.__lt__(obj2)</kbd>). 
To enable sort operation on instances of a class we should implement the <em>__lt__</em> special method. e.x.:<br>
<pre class=prettyprint>
def __lt__(self, other):
    """return True if self's name is lexicographically
       less than other's name, and False otherwise"""
    if self.lastName == other.lastName:
        return self.name < other.name
    return self.lastName < other.lastName</pre><br>
<li>Assume we have a class which defines operations on a set. If we want <kbd>len(s)</kbd> return the number of members of s, then we need to define <em>len</em> using underscores:<br>
<pre class=prettyprint>
def __len__(self):
    count = 0
    for i in self.vals:
        count += 1
    return count
</pre><br>
If we don't use underscores, we have to get the length using <kbd>s.len()</kbd></li>
<li><b>Inheritance</b><br>
<pre class='prettyprint'>
class Person(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name

class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign
    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum

class UG(MITPerson):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year

class Grad(MITPerson):
    pass

def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad)</pre><br>
</ul>
As Python has no concept of private variables, leading underscores are used to indicate variables that must not be accessed 
from outside the class. So using local variable names beginning with an underscore is discouraged.
</div>
</details>


### Generators
<pre class="prettyprint">
def genTest():
    yield 1
    yield 2
foo = genTest()
print foo.next()
print foo.next()
print foo.next()
#---------- alternatively
for n in foo:
    print n</pre>
```python

1
2
StopIteration Exception

1
2
```<br>
<pre class="prettyprint">
def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        next = fibn_1 + fibn_2
        yield next
	fibn_2 = fibn_1
	fibn_1 = next
fib = genFib()
for i in range(5):
    print fib.next()</pre>
```python
1 2 3 5 8
```<br>
<b>Generator Expressions</b> (alternative of list comprehention to save memory)<br>
The first example above can be written as follows<br>
<pre class="prettyprint">
foo = (i for i in xrange(2))
</pre><br>

<pre class="prettyprint">
a = xrange(3)
print list(a)
print tuple(a)
print set(a)
b=['a','b','c']
print dict(zip(a,b))</pre>

```python
[0, 1, 2]
(0, 1, 2)
set([0, 1, 2])

{0: 'a', 1: 'b', 2: 'c'}

```<br>
    </div>
</details>



### Misc.

    <details class="details">
        <summary><div class="wrapper"><b>print</b></div></summary>
        <div class="content">
<pre class="prettyprint">
a=['a', 'b', 'c']
for index, item in enumerate(a):
    print '%d. %s' % (index, item)


</pre>
```python

0. a
1. b
2. c
```<br>

<pre class="prettyprint">
first_name ='John'
last_name = 'Doe'
print "Full name is {} {}".format(first_name, last_name)
</pre>
```python
Full name is John Doe
```<br>
* in Python 3.6+ we can use F-Strings insted: <samp>print(f"Full name is {first_name} {last_name}")</samp><br>
<br>
For printing members of <samp>myList</samp> line by line: <samp>print(*myList, sep='\n')</samp><br><br>	
</div>
</details>

	    
<details class="details">
    <summary><div class="wrapper"><b>Input</b></div></summary>
    <div class="content">
<pre class=prettyprint>
with open('pathToFile', [option]) as f:
  fl = f.readlines()
data = [ eval(line.rstrip('\n')) for line in fl ]
X1, ..., Xn = zip(*data) 
</pre><br>
[option] can be <samp>'r'</samp> (read) [default], <samp>'w'</samp> (write), <samp>'r+'</samp> (read and write) and <samp>'a'</samp> (append).<br>
<br>
<kbd>fl = f.readlines()</kbd> turns f into a list of strings, each item of list is one line of f (defined by '\n')<br>
<kbd>fs = f.read()</kbd> turns f into one string<br>
<kbd>l = f.readline()</kbd> reads the first line as a string<br>
<br>
<pre class=prettyprint>guess = 50
x = raw_input('Is your number ' + str(guess) + '?' + '\n Enter \'Yes\' or \'No\': ')

</pre>
```python
Is your number 50?
Enter 'Yes' or 'No':
```<br>
</div>
</details>

<details class="details">
    <summary><div class="wrapper"><b>copying</b></div></summary>
    <div class="content">
<a href="https://stackoverflow.com/a/3975388/2445273">This</a> explains the difference between reference assignment, shallow copying and deep copying.<br>
<kbd>[:]</kbd> makes a shallow copy of a string or list.
<kbd>dic.copy()</kbd> do the same for dictionaries.<br>
If our list is a list of lists or list of objects (similar for dictionaries), then we need to do deep copying so that altering the copy doesn't alter the original:<br>
<pre class="prettyprint">
import copy
list2 = copy.deepcopy(list1)</pre><br>
</div>
</details>

<details class="details">
    <summary><div class="wrapper"><b>Divisions</b></div></summary>
    <div class="content">
```python
9%2
9/2
-9/2
9.0/2
9/2.0
9.0/2.0
```
```python
1
4
5
4.5
4.5
4.5
```<br>
*In Python 3.x 9/2 = 4.5. We can achieve this in Python 2.2+ with <kbd>from __future__ import division;</kbd>
</div>
</details>


<details class="details">
    <summary><div class="wrapper"><b>Sorting</b> a list with <b>two rules</b></div></summary>
    <div class="content">
```python
l=[(4,'mouse'),(1,'cat'),(3,'horse'),(2,'pog'),(3,'cow'),(2,'dog')]
l.sort(key=lambda x: (-x[0], x[1]))
```
```python
[(4, 'mouse'), (3, 'cow'), (3, 'horse'), (2, 'dog'), (2, 'pog'), (1, 'cat')]
```<br>
If an element is a calss instance, we need to use dot notation. E.x.<br>
```python
l.sort(key=lambda x: (x[0].name, x[1].age))
```
</div>
</details>

<details class="details">
    <summary><div class="wrapper">Measure the <b>runtime</b> of a program</div></summary>
    <div class="content">
<pre class="prettprint">
import time
start = time.time()
[body]
end = time.time()
print end - start
</pre><br>
Another way is from shell: <kbd>time python [py file]</kbd><br>
<br>
For small bits of Python code we can use <samp>timeit</samp> (it can be run from <a href="https://docs.python.org/2/library/timeit.html#python-interface">python interface</a> as well): <br>
<kbd>python -m timeit [-n N] [-r N] [statement ...]</kbd><br>
where 
<samp>-n N, (--number=N)</samp> denotes how many times to execute ‘statement’, and <samp>-r N, (--repeat=N)</samp> denotes how many times to repeat the timer (default 3).
</div>
</details>

	    
	    
<details class="details">
    <summary><div class="wrapper">time</div></summary>
    <div class="content">
<pre class="prettyprint">import time
from datetime import datetime
time.time()  # returns the value of time in seconds since the Epoch.
datetime.strftime('%Y-%m-%d %H:%M:%S')  # convert datetime to date string
datetime.strptime(t, "%Y-%m-%d %H:%M:%S.%f")  # convert date string to datetime
myDate.timestamp()  # convert datetime to epoch
datetime.fromtimestamp(t)  # convert epoch to datetime
</pre>
</div>
</details>

	    
	    
<details class="details">
    <summary><div class="wrapper"><b>Random Numbers</b></div></summary>
    <div class="content">
<pre class="prettyprint">
import random

r_num1 = random.random()  			# random float in [0, 1)
r_num2 = random.randrange(a, b)  		# random integer in [a, b)
r_num3 = random.uniform(a, b)  			# random float in [a, b)
r_num4 = random.normalvariate(mu, sigma)  	# random float from normal dist of mu and sigma

shuffled_list = random.shuffle(my_list)  	# shuffles the list
chosen_member = random.chice(my_list)  		# chooses a member of the list
chosen_members = random.sample(my_list, 4)  	# chooses 4 member of the list without replacement 
chosen_members_with_replacement = [random.choice(my_list) for _ in range(3)]

# use random.seed to get reproducible results
random.seed(5)
print random.random()  # 0.62290169489
random.seed(5)
print random.random()  # 0.62290169489
</pre><br>
</div>
</details>

<details class="details">
    <summary><div class="wrapper"><b>zip</b></div></summary>
    <div class="content">
<pre class="prettyprint">
zip(['a', 'b', 'c'], [1, 2, 3])  # [('a', 1), ('b', 2), ('c', 3)]
zip(('a', 1), ('b', 2), ('c', 3))  # [('a', 'b', 'c'), (1, 2, 3)]
data = [('a', 1), ('b', 2), ('c', 3)]
zip(*data)  # [('a', 'b', 'c'), (1, 2, 3)]
</pre><br>
</div>
</details>

<details class="details">
    <summary><div class="wrapper">Running <b>Bash</b> Commands inside Python</b></div></summary>
    <div class="content">
<pre class="prettyprint">
import subprocess
subprocess.call("BASH Command", SHELL=True)
</pre><br>    
</div>
</details>
	    
<details class="details">
    <summary><div class="wrapper"><b>*args and **kwargs</b></div></summary>
    <div class="content">
The general use of these is to produce higher-order functions whose inputs can accept arbitrary arguments.<br>
When we define a function using *args and **kwargs, args is a tuple of its unnamed arguments
and kwargs is a dict of its named arguments:<br>
<pre class="prettyprint">
def test(*args, **kwargs):
    print "unnamed args:", args
    print "keyword args:", kwargs

test(1, 2, key="word", key2="word2")  # unnamed args: (1, 2)
                                      # keyword args: {'key2': 'word2', 'key': 'word'}
</pre><br>
It works the other way too:<br>
<pre class="prettyprint">
def test2(x, y, z):
    return x + y + z

list123 = [1, 2, 3]
print(test2(*list123))  # 6
dict123 = {'a': 1, 'b': 2, 'c': 3}
print(test2(*dict123))  # 'abc'
print(test2(**dict123))	# 6
</pre><br>
</div></details>
<details class="details">
    <summary><div class="wrapper"><b>matplotlib</b></div></summary>
    <div class="content">
<pre class="prettyprint">
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))	# change the size of plot. Also fig.set_size_inches(10,5)
plt.axis([x_start, x_end, y_start, y_end])
plt.xticks(tick_list)
plt.xlabel("x_Label")
plt.ylabel("y_label")
plt.title("Title")
plt.legend(loc=9)  # assuming 'label' is defined. 9 means top-center
plt.grid(True)  # more options: plt.grid(color='r', linestyle='-.', linewidth=2)
plt.show()
</pre><br>

<b>Types of plots</b><br>
<pre class="prettyprint">
#--- Line Chart ---
plt.plot(x_list, y_list, color='green', marker='o', linestyle='solid', label='my_label', linewidth=2)  
# The arguments color/marker/linestyle can be shortened, e.g. 'go-'. 
# full list of arguments can be found <a href="https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html">here</a>.

#--- Bar Chart ---
plt.bar(x_list, y_list, bar_width)
# full list of arguments can be found <a href="https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html">here</a>.

#--- Scatterplots ---
plt.scatter(x_list, y_list,
		s=30, 		# marker size 
		alpha=.65,  	# alpha helps to show overlapping data
		color='b')
</pre><br>

<b>Annotation</b><br>
<pre class="prettyprint">
x_list = [...]
y_list = [...]
labels = [...]

plt.scatter(x_list, y_list)

# label each point
for label, x_item, y_item in zip(labels, x_list, y_list):
    plt.annotate(label,
        xy=(x_item, y_item),  # put the label with its point
        xytext=(5, -10),  # but slightly offset
        textcoords='offset points')

# full list of arguments can be found <a href="https://matplotlib.org/api/_as_gen/matplotlib.pyplot.annotate.html">here</a>.
</pre><br>
<b>Misc.</b><br>
<pre class="prettyprint">
plt.axis("scaled")  # Equal scaling by changing box dimensions
# full list of arguments can be found <a href="https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis">here</a>.
</pre><br>

<b>Contours</b> are used to visualize 3D plot in 2D<br>
<pre class="prettyprint">
x = np.arange(0, 1, 0.1)
y = np.arange(0, 1, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True)
z = xx + yy
c = plt.contour(x, y, z) # representing a 3-dimensional surface by plotting constant z slices, called contours, on a 2-dimensional format.
plt.clabel(c, inline=1, fontsize=10)
</pre>
</div>
</details>


<details class="details">
    <summary><div class="wrapper"><b>sys</b></div></summary>
    <div class="content">
        <kbd>sys.argv</kbd> is the list of command-line arguments. So <samp>sys.argv[0]</samp> is the name of the program itself
    </div>
</details>

<details class="details">
    <summary><div class="wrapper"><b>re</b></div></summary>
    <div class="content">
<pre class=prettyprint>
import re
msg = "hi, this is a test"
re.findall('.*s', msg)[0]  # ['hi, this is a tes']
re.findall('.*?s', msg)[0]  # ['hi, this', ' is', ' a tes']  non-greedy search
re.findall('\w+', msg)[0]  # ['hi', 'this', 'is', 'a', 'test'] \w = [A-Za-z0-9_]
re.match('.*"(.*),(.*).*"', row)  # if it doesn't match anything returns None. So it can be used in conditionals
re.sub('(.*)abc(.*)"', '"\g&lt;1&gt;\g&lt;2&gt;"', row)  # refer to matched groups using \g&lt;n&gt; 
try:
    extracted_pattern = re.search('AAA(.+?)ZZZ', text).group(1)  # equivalent of perl -pe 's/AAA(.+?)ZZZ/\1/' test
except AttributeError:
    extracted_pattern = ''
</pre><br>
Matching the part that starts with an space followed by / (without including the space in the result) until a space 
(without including the space):<br>
<samp>re.findall('(?&lt;=\s)/[^\s]*', log_msg)[0]  # ?&lt;=</samp>  is called 'lookahead'<br>
    </div>
</details>

<details class="details">
    <summary><div class="wrapper"><b>Web Scraping</b></div></summary>
    <div class="content">
        <pre class=prettyprint>
import requests
from bs4 import BeautifulSoup

url = 'http://...'

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text
html = r.text	# This is a string. If the url returns json (e.x. API call, for a dict use r.json())

soup = BeautifulSoup(html)
pretty_soup = soup.prettify()
print(pretty_soup)

print(soup.title())
print(soup.get_text()) # apparently get_text() doesn't work on prettified soups


def get_all_urls(soup):
  """ finds all urls in the page and return them as a list"""
  return [link.get('href') for link in soup.find_all('a')]

tag_elements = [tag_element for tag_element in soup.find_all('a')]
all_urls = [url + tag_element.get('href') for tag_element in soup.find_all('a')]
all_urls_texts = [tag_element.contents[0] for tag_element in soup.find_all('a')]</pre><br>
The package <a href="https://newspaper.readthedocs.io/en/latest/" > newspaper </a> is practical and useful.
    </div>
</details>
	
	
	
	
<ul>
	<li> <b>Difference between <kbd>==</kbd> and <kbd>is</kbd></b><br>
    The equality operator (<kbd>x == y</kbd>) tests the values of x and y for equality, while the identity operators (<kbd>is</kbd>) tests two objects to see whether they refer to the same object in memory. 
    In general, it may be the case that <kbd>x == y</kbd>, but <kbd>x is not y</kbd>.<br>
<code>
>>> a = [1, 2, 3]<br>
>>> b = a<br>
>>> b is a <br>
<span style="color:blue">True</span><br>
>>> b == a<br>
<span style="color:blue">True</span><br>
</code>
<code>
>>> a = [1, 2, 3]<br>
>>> b = a[:]<br>
>>> b is a<br>
<span style="color:blue">False</span><br>
>>> b == a<br>
<span style="color:blue">True</span>
</code></li>
	<li><kbd>dir</kbd> lists attributes of an object. E.g. <sampl>dit("hi")</samp> lists all strng methods.
	<li><b>Prettyprint</b>ing structured data: <br>
		<pre class=prettyprint>
import pprint
pprint.pprint(structuredData)</pre><br>
		
<pre class=prettyprint>
import pprint
import requests
import json

response = requests.get("URL")
pprint.pprint(json.loads(response.text))</pre>

	<li><kbd>inspect</kbd> is handy for looking at source code modules:<br>

<pre class=prettyprint>
import inspect
import queue	# Python 3
print(inspect.getsource(queue))</pre>
	<li><kbd>sh</kbd> module makes it easy to work with standard os and subprocess libraries:<br>
		<pre class=prettyprint>
import sh
sh.pwd()
sh.mkdir('newDir')
sh.touch('newFile.txt')
sh.whoami()
sh.echo('This is cool!')</pre><br>
<kbd>pythonpy</kbd> is the opposite. Uses python is command-line.
</ul>
	    
	    
    </div>
</details>	
	
</body>
</html>
