# Q1: Convert list into tuple and unpack values.
lst = [1, 2, 3, 4]
t = tuple(lst)

a, b, c, d = t
print(a, b, c, d)


# Q2: Extract second values from tuple of tuples.
t = (('a', 1), ('b', 2), ('c', 3))
result = [x[1] for x in t]
print(result)


# Q3: Return sum, min, max from a tuple of numbers.
def calculation(nums):
    return sum(nums), min(nums), max(nums)

sum_val, min_val, max_val = calculation([2, 5, 1, 8])
print(sum_val, min_val, max_val)


# Q4: Concatenate two tuples and convert into list.
t1 = (1, 2, 3)
t2 = (4, 5)

result = list(t1 + t2)
print(result)


# Q5: Find most frequent element in tuple.
t = (1, 2, 3, 3, 3, 4)
freq = max(set(t), key=t.count)
print(freq)


# Q6: Check if two tuples have same elements (order independent).
t1 = (1, 2, 3)
t2 = (3, 2, 1)
print(sorted(t1) == sorted(t2))


# Q7: Slice last 3 elements from tuple.
t = (1, 2, 3, 4, 5, 6)
print(t[-3:])


# Q8: Repeat tuple elements.
t = (1, 2)
print(t * 3)


# Q9: Flatten nested tuple.
t = ((1, 2), (3, 4))
flat = tuple(x for sub in t for x in sub)
print(flat)


# Q10: Calculate Manhattan distance between two points.
p1 = (2, 3)
p2 = (5, 7)

distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
print(distance)