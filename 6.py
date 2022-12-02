#1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#    *Пример:*
#    - Для N = 5: 1, -3, 9, -27, 81

#i = int(input('Введите число N: '))
#y = 1
#while i >= 1:
#    print(int(y))
#    y = y * (-3)
#    i = i - 1



#2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#    *Пример:*
#    - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

#i = int(input('Введите число N: '))
#for n in range (1,i + 1):
#    n = (n * 3) + 1
#    print(n, end = ', ')

    
#3. Напишите программу, в которой пользователь будет задавать две строки, 
#а программа - определять количество вхождений одной строки в другой.
s = input('Введите строку ')
k = input('Что ищем ')
#x = s.count(k)
#print(x)
count2 = 0
count1 = 0
for i in range (0,len(s)):
    
    for j in range (0,len(k)):
        if s[i] == k[j]:
            count1 +=1
    print(count1)
    if count1 == len(k):
        count2 += 1
    count1 = 0
        
print(count2)
s1 = input()
s2 = input()
print(s1.count(s2))

s1 = 'ЯлюблюлюблюлюблюPython'
s2 = 'люблю'
i = 0
cnt = 0
while i < len(s1) - 1:
    if s1[i:len(s2) + i] == s2:
        cnt += 1
    i += 1
print(cnt)

s1 = 'ЯлюблюлюблюлюблюPython'
s2 = 'лю'
cnt = 0
while s2 in s1:
    s1 = s1.replace(s2, ' ', 1)
    print(s1)
    cnt += 1
print(cnt)

s1 = 'Я люблю люблюлюблюPython'
s2 = 'лю'
res = s1.split(s2)
print(res)
print(len(res) - 1)
