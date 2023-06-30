# FizzBuzz is a classic interview question. The goal is to print the numbers from 1 to 100. However, if the number is a multiple of 3, 5, or both 3 and 5, print "Fizz", "Buzz", or "FizzBuzz", respectively. 

for i in range(1, 101):
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