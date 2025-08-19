n=int(input("enter number"))
power=len(str(n))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**power
    temp=digit
if n==sum:
    print(n,"is an armstrong number")
else:

    print(n,"is not an armstrong number")
