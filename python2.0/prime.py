
a=int(input("enter num="));

isprime = True

for i in range(2,a-1):
    if(a%i==0):
        isprime=True
        
    else:
       isprime=False

# print(isprime)
if(isprime=True):
    print("num isprime")
else;
    