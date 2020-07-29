def calculate_fibonacci(number):
    if number == 1 or number == 2:
        return 1;
    if number == 0:
        return 0 
    
    return calculate_fibonacci(number-1) + calculate_fibonacci(number-2)


print(calculate_fibonacci(9))
print(calculate_fibonacci(10))