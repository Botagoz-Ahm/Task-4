def IsPointInSquare(x,y):
    if (x**2+y**2)**0.5 <=(2)**0.5:
         return 'Yes'
    else:
         return 'No'
x = float(input())
y = float(input())
print(IsPointInSquare(x,y))
