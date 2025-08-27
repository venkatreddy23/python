#List methods


#slicing
list1=[1,2,34,5,88,6,86,0]
print(list1[2:6])  #[34, 5, 88, 6]

#len()
print(len(list1))   #8

#in
print(5 in list1)  #True

#concatination
list2=[33,77,69,22,43,9]
print(list1+list2)  #[1, 2, 34, 5, 88, 6, 86, 0, 33, 77, 69, 22, 43, 9]

#append
list1.append([9])
print(list1)   #[1, 2, 34, 5, 88, 6, 86, 0, [9]]

#extend
list1.extend(['2',3,[6]])
print(list1)    #[1, 2, 34, 5, 88, 6, 86, 0, [9], '2', 3, [6]]

#insert
list2.insert(2,79)
print(list2)   #[33, 77, 79, 69, 22, 43, 9]

#remove
list2.remove(69)
print(list2)  #[33, 77, 79, 22, 43, 9]

#pop()
print(list2.pop(2))   #79
print(list2)    #[33, 77, 22, 43, 9]

#index()
print(list2.index(22))  #2

#reverse()
list2.reverse()
print(list2)    #[9, 43, 22, 77, 33]

#sort()
list3=['ant','goat','pen','hill','bag','zip']
list2.sort(reverse=True)
list3.sort()
print(list3)    #['ant', 'bag', 'goat', 'hill', 'pen', 'zip']
print(list2)    #[77, 43, 33, 22, 9]

#clear()
list2.clear()
print(list2)   #[]




#set Methods

#add()
set1={1,3,4,5,6,6,55,'8'}
set1.add(22)
print(set1)   #{1, 3, 4, 5, 6, 55, 22, '8'}

#remove()
set1.remove(6)
print(set1)  #{1, 3, 4, 5, 55, 22, '8'}

#discard()
set1.discard(8)
print(set1)   #{1, '8', 3, 4, 5, 55, 22}
set1.discard('8')
print(set1)   #{1, 3, 4, 5, 55, 22}


#pop()
set2={2,3,8,9,88}
print(set2.pop())  #2

#clear()
set2.clear()
print(set2)    #set()

#union()
set1={1,3,4,5,6,6,55,'8'}
set2={2,3,8,9,88}
print(set1.union(set2))     #{1, 2, 3, 4, 5, 6, '8', 8, 9, 55, 88}

#intersection()
print(set1.intersection(set2))    #{3}

#difference()
print(set1.difference(set2))    #{1, 4, 5, 6, '8', 55}

#symmetric_difference
print(set1.symmetric_difference(set2))   #{1, 2, 4, 5, 6, 8, 9, '8', 88, 55}


#issubset
print(set1.issubset(set2))   #False

#issuperset
set3={1,3}
print(set1.issuperset(set3))   #True

# isdisjointset()
set4={"33",45,73}
print(set4.isdisjoint(set1))   #True








