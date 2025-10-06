#                -------------------------------EASY-----------------------------------

#1   Check if a number is even or odd.
# def even_or_odd(num):
#     if num%2 == 0:
#         return "even"
#     return "odd"
# number = int(input("enter thr number"))
# print(even_or_odd(number))


#2  Find the maximum and minimum element in a list.
# def max_min(list1,max,min):
#  if not list1:
#     return "empty list"
#  max = list1[0]
#  min =  list1[0]
#  for i in list1:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
#  return "max =",max,"min =",min
# list2 = [11,23,65,78,3,6,92]

# print(max_min(list2,max,min))


#3  Reverse a string without using slicing ( [::-1] ).
# str1 = "Jai Bob"
# str2 = ""
# for i in str1:
#     str2 = i + str2
# print(str2)


# def revstr(str):
#     if len(str) == 0:
#         return str
#     return revstr(str[1:]) + str[0]
# print(revstr("jai bob"))


#4  Check if a string is a palindrome.
# str1 = "malayalam"
# i = 0
# j = len(str1) - 1
# flag = True
# while i < j:
#     if str1[i] != str1[j]:
#         flag = False
#         break
#     i += 1
#     j -= 1
# if flag:
#     print("palindrome")
# else:
#     print("not a palindrome")


#5  Find the factorial of a number (using loop).
# num = 5
# temp = num
# prd = 1
# while temp > 1:
#     prd = temp*prd
#     temp -= 1
# print(prd)


#6  Count the frequency of each character in a string.
#frequency
# str1 = "madam"
# str2 = ""
# freq = []
# for i in str1:
#     if i not in str2:
#         str2 += i
#         count = 0
#         for j in str1:
#             if i == j:
#                 count += 1
#         freq.append(count)
# for k in range(len(str2)):
#     print(str2[k], freq[k])


#7  Find the second largest number in a list.
# l1 = [11,20,34,98,70]
# max1 = max2 = float('-inf')
# for i in l1:
#     if i > max1:
#         max2 = max1
#         max1 = i
#     elif i > max2 and i != max1:
#         max2 = i
# print(max2)


#8  Count how many vowels and consonants are in a string.
# str1 = "Develop"
# vcount = 0
# ccount = 0
# for i in str1:
#     if i in 'aeiouAEIOU':
#         vcount += 1
#     else:
#         ccount += 1
# print(vcount,ccount)


#9  sum of digits of a number
# num = 123
# temp = num
# sum = 0
# while temp > 0:
#     rem = temp % 10
#     sum += rem
#     temp //= 10
# print(sum)


#10  multiplication table
# num = 6
# for  i in range(1,11):
#     print(num,'x',i,'=',num*i)


#11  largest word in a sentence
# str = "the  brown fox"
# str1 = str.split()
# str2 = ""
# for i in str1:
#     if len(i)  > len(str2):
#         str2 = i
# print(str2)


#12   Remove all duplicate elements from a list.
# l1 = [11,21,21,11,33,31,11,5,4,5,31]
# l2 = []
# for i in l1:
#     if i not  in l2:
#         l2.append(i)
# print(l2)


#13  Sort a list without using Python’s built-in .sort() .
# list1 = [97, 43, 2, 22, 65, 98]
# for i in range(0,len(list1)):
#     for j in range(0,len(list1) - 1 - i):

#      if list1[j] > list1[j+1]:
#         list1[j], list1[j+1] = list1[j+1] ,list1[j]
# print(list1)


#14  Merge two lists into a single sorted list.
# list1 = [97, 43, 2, 22, 65, 98]
# list2 = [69, 98, 3, 66, 97, 34]
# for i in range(len(list1)):
#     for j in range(len(list1) - 1 - i):
#         if list1[j] > list1[j+1]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]
# for i in range(len(list2)):
#     for j in range(len(list2) - 1 - i):
#         if list2[j] > list2[j+1]:
#             list2[j], list2[j+1] = list2[j+1], list2[j]
# merge = []
# i = j = 0
# while i < len(list1) and j < len(list2):
#     if list1[i] < list2[j]:
#         merge.append(list1[i])
#         i += 1
#     else:
#         merge.append(list2[j])
#         j += 1
# merge.extend(list1[i:])
# merge.extend(list2[j:])
# print(merge)



#15  Check if a number is a prime number.
# n = int(input("enter number"))
# if n <= 1:
#     print("not a prime")
# flag = True
# for i in range(2,int(n**0.5) + 1):
#     if n % i == 0 :
#         # print("not a prime")
#         flag = False
#         break
# if flag:
#         print("prime")
# else:
#         print("not a prime")






#                -------------------------------MEDIUM-----------------------------------











#1   Find all pairs in a list that sum up to a target value.
# def equal_sum(list1,sum):
#     pairs = []
#     for i in range(len(list1)):
#         for j in range(i+1,len(list1)):
#             if list1[i] + list1[j] == sum:
#                 pairs.append((list1[i],list1[j]))
#     return pairs
# list2= [2,4,6,1,3,7,9,8]
# print(equal_sum(list2,10))   #[(2, 8), (4, 6), (1, 9), (3, 7)]


#2  Implement a program to rotate a list by k positions.
# def list_rotate(list1,k):
#  n = len(list1)
#  k = k % n
#  return list1[-k:] + list1[:-k]
# list1 = [2,4,5,6,9]
# print(list_rotate(list1,3))  #[5, 6, 9, 2, 4]


#3   Find the missing number in a list of consecutive integers.
# def missing_num(list1):
#  list2 = []
#  for i in range(1,max(list1)):
#     if i not in list1:
#         list2.append(i)
#  return list2
# list1 = [1,2,3,4,5,6,9]
# print(missing_num(list1))


#4  Check if two strings are anagrams.
# def anagrams(str1,str2):
#    return "anagrams" if sorted(str1) == sorted(str2) else "not anagrams"
# print(anagrams("ten","net"))


#5  Count the number of words in a sentence.
# def w_count(sentence):
#     return len(sentence.split())
# print(w_count("Count the number of words in a sentence"))


#6  Remove all duplicate words from a sentence.
# str1 = "one two one three two four"
# str2 = str1.split()
# st2 =[]
# for  i in str2:
#    if i not in st2:
#       st2.append(i)
# print(st2)


#7  Given a dictionary, invert it (keys become values).
# def invert(ditr):
#     return {values: keys for keys, values in ditr.items()}
# ditr = {1:"aa", 2:"bb", 3:"cc", 4:"dd"}
# print(invert(ditr))


#8  Find the intersection of two lists.
# def intersection(list1, list2):
#     return (set(list1) & set(list2))
# print(intersection([1,2,3,4,5],[3,4,5,6,7]))


#9  Print the transpose of a matrix.
# list1 = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# for i in range(0,len(list1)):
#     for j in range(0,len(list1)):
#        if i < j:
#         list1[i][j], list1[j][i]= list1[j][i],list1[i][j]
# print(list1)


#10   Implement bubble sort.
# def bubblesort(list1):
#  for i in range(0 ,len(list1)):
#     for  j in range(0,len(list1)- 1 - i):
#         if list1[j] > list1[j+1]:
#             list1[j] , list1[j+1] = list1[j+1], list1[j]
#  return list1
# list1 = [1,12,13,56,78,96,23,55,77]
# print(bubblesort(list1))


#11  Find the first non-repeating character in a string.
# def n_repeat(str):
#     for i in str:
#         for j in str:
#             if  i != j:
#                 return j
#     return None
# print(n_repeat("success"))


#12  Find the longest word in a sentence.
# def longest_word(str1):
#     long = ""
#     words = str1.split()
#     for i in words:
#         for j in words:
#             if i > j:
#                 long = i
#     return long
# print(longest_word("Find the longest word in a sentence"))
 

#13  Find the second smallest number in a list.
# def smallest(lis1):
#   min1 = float('inf')
#   min2 = float('inf')
#   for  i in list1:
#     if i < min1:
#         min2 = min1
#         min1 = i
#     elif min1 < i < min2:
#         min2 = i 
#   return min2
# list1 = [1,12,3,4,5,44,65,76,2]
# print(smallest(list1))


#14  Implement a program to check if a number is an Armstrong number.
# num = 153
# count = 0
# sum = 0
# temp = num
# while temp > 0:
#     count += 1
#     temp = temp  //10
# temp = num
# while temp  >  0:
#         d = temp % 10
#         sum = sum + (d**count)
#         temp = temp // 10
# if sum == num:
#     print("armstrong")
# else:
#     print("not")



