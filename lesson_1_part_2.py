number = None
while True:
    number = int(input('Ввведите число от 0 до 10: '))
    if number < 10:
        break
    print('Вы ввели неверное число')
print(number**2)
