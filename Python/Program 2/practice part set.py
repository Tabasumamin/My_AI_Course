# Q1: Difference between two sets
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a - b)


# Q2: Intersection of three sets
a = {1, 2, 3}
b = {2, 3, 4}
c = {3, 5, 2}
print(a & b & c)


# Q3: Convert sentence into unique words using set
sentence = "Python is a powerful language"
words = set(sentence.lower().split())
print(words)


# Q4: Remove duplicates from list and sort
lst = [4, 1, 2, 2, 3, 1]
result = sorted(set(lst))
print(result)


# Q5: Check subset relationship
a = {1, 2}
b = {1, 2, 3}
print(a < b)


# Q6: Set comprehension (squares of numbers divisible by 3)
result = {x*x for x in range(1, 16) if x % 3 == 0}
print(result)


# Q7: Count duplicate elements in list
lst = [1, 2, 2, 3, 4, 4, 5]
duplicates = len(lst) - len(set(lst))
print(duplicates)


# Q8: Remove vowels from string
vowels = {'a', 'e', 'i', 'o', 'u'}
text = "Malik Waqas"
result = ''.join([y for y in text.lower() if y not in vowels])
print(result)


# Q9: Symmetric difference of sets
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)


# Q10: Check if two strings are anagrams (set-based approach)
a = "listen"
b = "silent"
print(set(a) == set(b))