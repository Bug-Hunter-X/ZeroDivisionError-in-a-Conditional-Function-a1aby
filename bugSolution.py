def function_with_uncommon_error_solution(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif b != 0:
        return a / b
    else:
        return 0 #Handle the case where both are zero. 

result = function_with_uncommon_error_solution(5, 0)
print(result) #This will give 5
result = function_with_uncommon_error_solution(0,5)
print(result) #This will give 0
result = function_with_uncommon_error_solution(5,5)
print(result) #This will give 1.0
result = function_with_uncommon_error_solution(0,0)
print(result) #This will give 0