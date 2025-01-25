def my_function(x):
    if x == 0:
        return float('inf') # Or handle it appropriately for your needs
    else:
        return 1 / x

print(my_function(0)) # Output: inf
print(my_function(5)) # Output: 0.2