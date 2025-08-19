n=int(input("enter number"))
d=len(str(n))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**d
    
    temp=digit
if n==sum:
    print("armstrong")
else:
    print("not")