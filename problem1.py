numbers = 12
# Write a lambda function and use map
digits = lambda x: sum(int(n) for n in str(x))
print(digits(numbers))