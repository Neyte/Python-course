import math

print('Введите длины сторон через пробел')
a,b,c=list(map(float,input().split()))
print(a, ', ', b, ', ', c)
p = (a+b+c)/2
S = math.sqrt(p * (p-a) * (p-b) * (p-c))
print('Площадь = ', S)
