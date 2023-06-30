# The Fibonacci sequence is another classic programming challenge. It's a sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The first few numbers of the sequence are:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# With these being the indeces:   
# 0, 1, 2, 3, 4, 5, 6,  7,  8,  9, ...
# So, the 8th number in the Fibonacci sequence is 21.

a, b = 0, 1             # a = 0; b = 1
for _ in range(10):     # no need to specify a variable name
    print(a)
    a, b = b, a + b     # a = b; b = a + b






# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34