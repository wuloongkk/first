numbers = list(map(int, input("Enter numbers separated by commas: ").split(',')))
evens = [num for num in numbers if num % 2 == 0]
print(evens)