p=int(input("Enter the principal amount :"))
t=int(input("Enter the time period :"))
g=input("Enter your gender (male/female): ")
s=input("Are you senior citizen?(y/n)")

if g=='female' and s=='y':
    r=8
elif g == 'female' and s == 'n':
    r=6
elif g == 'male' and s=='y':
    r=7
elif g == 'male' and s == 'n':
    r=5
else:
    print("Invalid Input")

simpleInterest=(p*t*r)/100
print("Simple Intrest is :",simpleInterest)
