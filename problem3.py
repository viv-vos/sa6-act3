
from functools import reduce
list1 = [1, 5, 77, 7]
max1 = reduce(lambda x, y: x if x > y else y, list1)
print(max1)