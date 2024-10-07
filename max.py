def max_value(list):
    
    max = list[0]
    for i in list:
       
        if i > max:
            max = i
    return max

num = [12, 65, 54, 39, 102, 37, 72, 33, 5, -28, 0, 15]
print(max_value(num))
