d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
top = {'b': 23, 'a': 119}
a = sorted(d.items(), key=lambda x: x[1])
b = sorted(top.items(), key=lambda x: x[1], reverse=True)
print(a, b)
