#string methods

#accessing
str1='I Love Cars and Bikes'
print(str1[0])   #I

# Slicing
print(str1[0:6])   #I Love

#concatination
str2='-gear head '
print(str1+str2)   #I love Cars and Bikes-gear head

#Repeatition
print(str2*3)    #-gear head -gear head -gear head

#strip()
str4='    benelli   600i  '
print(str4.strip())   #benelli   600i

#upper()
print(str1.upper())   #I LOVE CARS AND BIKES
print(str1.lower())   #i love cars and bikes

#find
print(str1.find('Car'))   #7
print(str1.find('raC'))   #-1

#replace
print(str1.replace('Cars','Automobile'))   #I Love Automobile and Bikes


#split()
strr='a,b,c'
print(strr.split('b'))    #['a,', ',c']


#join()
# str5=["'1','4','22'"]
str5=['a','b','4','7']
print('-'.join(str5))    #a-b-4-7

#startswith(prefix)
print(str1.startswith('I '))   #True

#endswith(suffix)
print(str1.endswith('es'))   #True


#count()
print(str1.count('e'))    #2





