def apply_all_func(int_list, *functions):
    results = {}
    
    for func in functions:
        try:
            result = func(int_list)
            results[func.__name__] = result
        except TypeError:
            print(f"Внимание: {func.__name__} не применимо к этому типу списка.")
    
    return results

numbers = [6, 20, 15, 9]

print(apply_all_func(numbers, max, min))
print(apply_all_func(numbers, len, sum, sorted))
