name = input('Как Вас зовут?:')
age = int(input('Введите сколько Вам лет:'))
weight = int(input('Введите сколько киллограм составляет Ваша масса тела:'))
if age <= 30 and 50 < weight < 120:
    print(name, age, 'год', 'вес', weight, '-хорошее состояние')
elif 40 > age >= 30 and (weight > 120 or weight < 50):
    print('требудется заняться собой')
elif age >= 40 and (weight > 120 or weight < 50):
    print(name, age, 'год', 'вес', weight, '-требуется врачебный осмотр')
else:
    print(name, age, 'год', 'вес', weight, 'Поздравляю, Вы абсолютно здоровы')
