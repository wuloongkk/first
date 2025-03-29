def all_digits_odd(n):
    return all(int(digit) % 2 != 0 for digit in str(n))

numbers = [num for num in range(1000, 3001) if all_digits_odd(num)]
print("@".join(map(str, numbers)))