def my_function(x):
    if x == 0:
        return 0
    else:
        return 1 / x

print(my_function(0)) # ZeroDivisionError
print(my_function(5)) # Output: 0.2