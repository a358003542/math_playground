def recursive_function(n, func, x):
    if n == 1:
        return func(x)
    else:
        return func(recursive_function(n-1, func, x))
def default_func(x):
    print(x)
    return x + 1

x = 1
recursive_function(5, default_func, x)