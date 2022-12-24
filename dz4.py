# 1)Вычислить число c заданной точностью d

pi = 3.141592653589793
t = float(input('Введите точность: '))
n = 0
while 1 > t:
    t *= 10
    n += 1

print(round(pi,n))


# 2)Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input('Введите число: '))
p = 2
while n > 1:
    if n % p == 0:
        print(p)
        n /= p
        p = 2
    else:
        p += 1 

# 3) Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
        
list = []
x = input('Введите список: ')
list = x.split(' ') 
for i in range(0, len(list)):
    if list.count(list[i]) < 2:
        print(list[i], end = " ")

# 4)Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
from random import randint

file = open('dz4.txt','w')
k = int(input('Введите степень: '))
while k > -1:
    x = randint(1, 100)
    if k > 1:
        file.write(str(x))
        file.write('*(x**')
        file.write(str(k)) 
        file.write(')+')
        
    elif k == 1:
        file.write(str(x))
        file.write('*x+')

    else:
        file.write(str(x))
    k -= 1
file.close()
