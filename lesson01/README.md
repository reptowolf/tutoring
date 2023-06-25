# Programming 101
This lesson will introduce you to the basic syntax of Python. Don't worry about memorizing anything. This is mostly to get you familiar with what python looks like and to give you a reference for later lessons.  
___

## 1 Variables and Types
Variables are used to store information. Python is dynamically typed, meaning you don't have to declare the type of a variable when you declare it. Python will figure it out. Here are some examples of different variable types:
```python
a = 5             # integer
b = "Hello"       # string
c = 3.14          # float
d = True          # boolean

# Collections are variables that can hold multiple values
e = [1, 2, 3]     # list[int]
f = (1, 2, 3)     # tuple[int]
g = {1, 2, 3}     # set[int]
h = {"a": 1}      # dictionary[str, int]
```
___

## 2 Functions
A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function: 
```python
def greet(name):
  print(f"Hello, {name}")

greet("Alice")      # prints: Hello, Alice
```
Functions can also return data as a result:
```python
def is_even(number):
  return number % 2 == 0

print(is_even(5))   # prints: False
```
___

## 3 Operators
Operators are also just functions, but they're a shorthand. Instead of writing `add(5,2)` you can write `5 + 2`. Here are some examples of operators:
```python
# math operators
print(5 + 2)      # addition:       (5 + 2)  == 7
print(5 - 2)      # subtraction:    (5 - 2)  == 3
print(5 * 2)      # multiplication: (5 * 2)  == 10
print(5 / 2)      # division:       (5 / 2)  == 2.5
print(5 // 2)     # floor division: (5 // 2) == 2
print(5 % 2)      # modulus:        (5 % 2)  == 1
print(5 ** 2)     # exponent:       (5 ** 2) == 25

# comparison operators
print(5 == 2)     # equality:       (5 == 2) == False
print(5 != 2)     # inequality:     (5 != 2) == True
print(5 > 2)      # greater than:   (5 > 2)  == True
print(5 < 2)      # less than:      (5 < 2)  == False

# boolean operators
print(True and False)  # and: (True and False) == False
print(True or False)   # or:  (True or False)  == True
print(not True)        # not: (not True)       == False
```
___

## 4 Control Structures
Control structures allow you to control the flow of your program. The main control structures in Python are `if`, `for`, and `while`.
```python
x = int(input("Enter a number: "))
if x > 0:
  print("The number you entered is positive")
elif x == 0:
  print("The number you entered is zero")
else:
  print("The number you entered is negative")
# Enter a number: 5
# The number you entered is positive
```
```python
for i in [0, 1, 2, 3, 4]:
  print(i)
# 0
# 1
# 2
# 3
# 4
```
```python
x = 5
while x > 0:
  print(x)
  x = x - 1
# 5
# 4
# 3
# 2
# 1
```
___
## 5 Examples
Again, this is mostly to get you familiar with what python looks like and to give you a reference for later lessons. Don't worry about trying to understand all of this yet, but I think seeing some more advanced examples will help you understand the basics better. 
___
### 5.1 FizzBuzz
FizzBuzz is a classic interview question. The goal is to print the numbers from 1 to 100, but for multiples of 3 print "Fizz" instead of the number, for multiples of 5 print "Buzz", and for multiples of both 3 and 5 print "FizzBuzz".
```python
for i in range(1, 101):
  # i is divisible by 3 and 5
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
```
___
### 5.2 Fibonacci
The Fibonacci sequence is another classic programming challenge. It's a sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The first few numbers of the sequence are:  
```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```  
With these being the indeces:   
```
0, 1, 2, 3, 4, 5, 6,  7,  8,  9, ...
```  
So, the 8th number in the Fibonacci sequence is 21. Here's one way to implement the Fibonacci sequence in Python:
```python
def fibonacci(n):
  a, b = 0, 1             # a = 0; b = 1
  for _ in range(n):      # no need to specify a variable name
    a, b = b, a + b       # a = b; b = a + b
  return a

print(fibonacci(8))  # prints: 21
```
There are always many ways to implement something. Here's another way to implement the Fibonacci sequence using a list:
```python
def fibonacci(n):
  nums = [0, 1]
  while len(nums) <= n:
    nums.append(nums[-1] + nums[-2])
  return nums[n]

print(fibonacci(8))  # prints: 21
```
And here's a recursive implementation. Recursion is when a function calls itself. This is a very common technique in programming, but it can be difficult to understand at first.
```python
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(8))  # prints: 21
```
___

### 5.3 Prime Numbers
A prime number is a number that is only divisible by 1 and itself. The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...
```python
def is_prime(n):
  if n < 2:
    return False
  for i in range(2, n):
    # try putting a print statement here to see what happens
    # print(f'{n} % {i} == {n % i}')
    if n % i == 0:
      return False
  return True
print(is_prime(5))  # prints: True
print(is_prime(10)) # prints: False
```
___

# 6 Practice
In programming, avoid the **illusion of competence**. Just because you can read code doesn't mean you can write code. The only way to get better at programming is to practice. Here are some resources to help you practice:
- [CodeWars](https://www.codewars.com/)
- [HackerRank](https://www.hackerrank.com/)
- [LeetCode](https://leetcode.com/)

While projects are the best way to improve at programming, sites like these are a great way to practice and learn new concepts. I recommend starting with CodeWars, as it's the most beginner friendly. HackerRank and LeetCode are more geared towards people grinding for competitive programming competitions or technical interviews.