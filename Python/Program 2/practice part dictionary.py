# Q1: Count frequency of words in a sentence
sentence = "python is fun and python is powerful"
d = {}
for word in sentence.split():
    d[word] = d.get(word, 0) + 1
print(d)


# Q2: Reverse a dictionary (key-value swap)
d = {'a': 1, 'b': 2, 'c': 3}
inv = {v: k for k, v in d.items()}
print(inv)


# Q3: Merge two dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'b': 5, 'c': 3}
result = {**d1, **d2}
print(result)


# Q4: Group words by first letter
words = ["apple", "banana", "apricot", "berry"]
d = {}
for word in words:
    d.setdefault(word[0], []).append(word)

print(d)


# Q5: Filter dictionary values greater than 50
d = {'a': 40, 'b': 60, 'c': 80}
result = {k: v for k, v in d.items() if v > 50}
print(result)


# Q6: Extract nested value using get()
data = {"user": {"profile": {"name": "Ali"}}}
name = data.get("user", {}).get("profile", {}).get("name")
print(name)


# Q7: Dictionary comprehension (cubes)
cubes = {x: x**3 for x in range(1, 11)}
print(cubes)


# Q8: Find key with maximum value
d = {'a': 10, 'b': 50, 'c': 30}
key = max(d, key=d.get)
print(key)


# Q9: Create dictionary using zip
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)


# Q10: Remove None values from dictionary
d = {'a': 1, 'b': None, 'c': 3}
result = {k: v for k, v in d.items() if v is not None}
print(result)