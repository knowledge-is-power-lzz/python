from functools import reduce

set_list = eval(input())  
result = reduce(lambda a, b: a | b, set_list)

print(result)