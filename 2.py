x = bool(input('Введите значение Х: '))
y = bool(input('Введите значение Y: '))
z = bool(input('Введите значение Z: '))
print('¬(X ⋁ Y ⋁ Z) =', (not(x or y or z)))
print('¬X ⋀ ¬Y ⋀ ¬Z =', (not x and not y and not z))