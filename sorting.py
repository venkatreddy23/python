#bubble sort
list1 = [111,22,-4,6,112,-55,46,3]
for i in range(0,len(list1)-1):
    for j in range(0,len(list1) - 1 - i):
        if list1[j] > list1[j+1]:
            flag = False
            list1[j], list1[j+1] = list1[j+1], list1[j]
print(list1)

#in descending order
list1 = [111,22,-4,6,112,-55,46,3]
for i in range(0,len(list1)-1):
    for j in range(0,len(list1) - 1 - i):
        if list1[j] < list1[j+1]:
            flag = False
            list1[j], list1[j+1] = list1[j+1], list1[j]
print(list1)

#based on the length of strings
str = ["cat","zebra","lion","dog", "cheetah"]
for  i in range(0,len(str)-1):
    for j in range(0,len(str)-1-i):
        if len(str[j]) > len(str[j+1]):
            str[j], str[j+1] = str[j+1], str[j]
print(str)


#nested list
str = [[22,99], [2,3], [6,9], [33,44],[15,9]]
for  i in range(0,len(str)-1):
    for j in range(0,len(str)-1-i):
        if str[j][0] > str[j+1][0]:
            str[j][0],str[j][1], str[j+1][0],str[j+1][1] = str[j+1][0],str[j+1][1], str[j][0],str[j][1]
print(str)

