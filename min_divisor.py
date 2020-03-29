def MinDivisor():

 if n%2==0:
    result=2
 elif n%3==0:
     result=3
 elif n%5==0:
     result=5
 elif n%7==0:
     result==7
 elif n%(n**0.5)==0:
     result=n ** 0.5
 else:
     result=n
 return result
n=int(input())
print(int(MinDivisor()))
