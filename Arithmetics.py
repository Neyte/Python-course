#print("А сейчас мы будем складывать числа... ")
#a=float(input("Первое число: "))
#b=float(input("Второе число: "))
#print("Сумма равна:",a+b)
from math import *
print("А сейчас будем решать квадратные уравнения")
a,b,c=list(map(float,input("Введите коефициенты через пробел:").split()))
print("получаем уравнение: ",a,"*x^2 + ",b,"*x + ",c," = 0")
discr = b*b - 4*a*c
if discr < 0:
    print("нет пути...")
elif discr == 0:
    print("X = ",b/2/a)
else:
    print("X1 = ",(-b+sqrt(discr))/(2*a))
    print("X2 = ",(-b-sqrt(discr))/(2*a))
