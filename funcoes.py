def print_numbers_recursive(number):
    print(number)
    if number <= 0:
        return False
    return print_numbers_recursive(number-1)

print_numbers_recursive(5)

