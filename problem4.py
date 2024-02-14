
list1 = [2, 5, 6, 7, 8, 9]
list2 = [2, 3, 1, 7, 10, 9]

intersection1 = list(filter(lambda x: x in list1, list2))

print(intersection1)
