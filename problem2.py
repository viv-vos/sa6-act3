list1 = ['apple', 'one', 'two', 'three']
words = sorted(list1, key = lambda x: (len(x), x))
print(words)
