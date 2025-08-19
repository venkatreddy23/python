n=int(input("enter number"))
power=len(str(n))
sum=0
temp=n
while temp>0:
    digit=temp%10
    num=digit**power
    sum+=num
    temp=temp//10
if n==sum:
    print(n,"is an armstrong number")
else:
    print(n,"not is not an armstrong number")
