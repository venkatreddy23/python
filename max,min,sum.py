def elme(list_input):
    if len(list_input) == 0:
        return "empty list"
    sum = 0
    max_ele = 0
    min_ele = list_input[2]
    
    for i in list_input:
        if i > max_ele:
            max_ele = i 
        if i < min_ele:
            min_ele = i
        sum += i
    return 'max ele-' ,max_ele,"min ele-",min_ele,"sum-",sum
list1=[22,55,66,77,89,9,-3,-6,8]
print(elme(list1))
