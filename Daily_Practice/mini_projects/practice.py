# numbers = [x + 1 for x in range(0,10)]
# square = [i ** 2 for i in range(1,11)]
# print(square)

# fruit = ["apple", "banana", "pineapple", "mango", "orange"]

# big_fruit = [i[0] for i in fruit]
# print(big_fruit)

numbers = [1, 2, 5, -3, -5, 2, 9]

negative = [i for i in numbers if i <= 0]
print(negative)