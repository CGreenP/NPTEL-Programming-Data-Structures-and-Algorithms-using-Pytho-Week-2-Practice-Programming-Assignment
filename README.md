# NPTEL-Python-Week-2-Practice-Programming-Assignment
NPTEL Python Week 2 Practice Programming Assignment

# Week 2 Practice Programming Assignment
1. Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n.

Here are some examples of how your function should work.
```python
>>> intreverse(783)
387

>>> intreverse(242789)
987242

>>> intreverse(3)
3
```

2. Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. Your function should return True if s has matched brackets and False if it does not.

Hint: Keep track of the nesting depth of brackets. Initially the depth is 0. The depth increases with each opening bracket and decreases with each closing bracket. What are the constraints on the value of the nesting depth for all brackets to be matched?

Here are some examples to show how your function should work.
```python
>>> matched("zb%78")
True

>>> matched("(7)(a")
False

>>> matched("a)*(?")
False

>>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
True
```

3. Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.

Here are some examples to show how your function should work.
```python
>>> sumprimes([3,3,1,13])
19

>>> sumprimes([2,4,6,9,11])
13

>>> sumprimes([-3,1,6])
0
```

# Sample Test Cases
|              | Input                                             | Output          |
|--------------|---------------------------------------------------|-----------------|
| Test Case 1  | intreverse(31511)                                 | 11513           |
| Test Case 2  | intreverse(4)                                     | 4               |
| Test Case 3  | intreverse(15135324234235)                        | 53243242353151  |
| Test Case 4  | matched("a3qw3;4w3(aasdgsd)((agadsgdsgag)agaga)") | True            |
| Test Case 5  | matched("(ag(Gaga(agag)Gaga)GG)a)33)cc(")         | False           |
| Test Case 6  | matched("(adsgdsg(agaga)a")                       | False           |
| Test Case 7  | matched("15ababa.agaga[][[[")                     | True            |
| Test Case 8  | sumprimes([101,93,97,44])                         | 198             |
| Test Case 9  | sumprimes([1001,393,743,59])                      | 802             |
| Test Case 10 | sumprimes([11,11,11,13,11,-11])                   | 57              |
| Test Case 11 | intreverse(31511)                                 | 11513           |
| Test Case 12 | intreverse(4)                                     | 4               |
| Test Case 13 | intreverse(15135324234235)                        | 53243242353151  |
| Test Case 14 | matched("a3qw3;4w3(aasdgsd)((agadsgdsgag)agaga)") | True            |
| Test Case 15 | matched("(ag(Gaga(agag)Gaga)GG)a)33)cc(")         | False           |
| Test Case 16 | matched("(adsgdsg(agaga)a")                       | False           |
| Test Case 17 | matched("15ababa.agaga[][[[")                     | True            |
| Test Case 18 | sumprimes([101,93,97,44])                         | 198             |
| Test Case 19 | sumprimes([1001,393,743,59])                      | 802             |
| Test Case 20 | sumprimes([11,11,11,13,11,-11])                   | 57              |
