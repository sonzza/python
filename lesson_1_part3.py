print('Добро пожаловать в медецинскую карту. Пожалуйста, следуйте инструкциям.')
name = input('Введите Ваше имя: ')
age = int(input('Введите Ваш возраст: '))
weight = int(input('Введите Ваш вес: '))

if 50 <= weight <= 120:
    print(name, ', ', age, ' лет, ', 'вес', weight, ' - хоть кто-то в хорошей форме')

else:
    if age < 30:
        print(name, ', ', age, ' лет, ', 'вес', weight,
              ' - начните питаться правильно и займитесь спортом, Вы в том возрасте, когда это еще просто')
    elif 30 <= age < 40:
        print(name, ', ', age, ' лет, ', 'вес', weight, '- Вам нужно заняться собой, часики-то тикают')
    else:
        print(name, ', ', age, ' лет, ', 'вес', weight, '- Вам следует срочно обратиться к врачу!')
