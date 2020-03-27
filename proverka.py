def IsPrime(n):
 if n ==2:
   return 'yes'
 if n==3:
   return 'yes'
 elif n==5:
   return 'yes'
 elif n==7:
   return 'yes'
 elif n%2==0:
   return 'no'
 elif n%3==0:
   return 'no'
 elif n%5==0:
   return 'no'
 elif n%7==0:
   return 'no'
 elif n%(n ** 0.5)==0:
   return 'no'
 else:
   return 'yes'
n=int(input())
print(IsPrime(n))

