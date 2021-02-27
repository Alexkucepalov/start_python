""" В этой игре человек загадывает число, а компьютер пытается его угадать. В начале игры человек загадывает число от
1 до 100 в уме или записывает его на листок бумаги. Компьютер начинает его отгадывать предлагая игроку варианты
чисел. Если компьютер угадал число, игрок выбирает “победа”. Если компьютер назвал число меньше загаданного,
игрок должен выбрать “загаданное число больше”. Если компьютер назвал число больше, игрок должен выбрать “загаданное
число меньше”. Игра продолжается до тех пор пока компьютер не отгадает число. Пример игры: Допустим, пользователь
загадал число 42 `15
35
96
<
37
74
<
52
<
42
=`
Примечание: Знаки “=”, “>” и “<” пользователь вводит с клавиатуры для общения с компьютером. Вы можете использовать
этот способ или придумать свой. """
import math

number = int(input('Введите число: '))


minNumber = 50
maxNumber = 100
print(minNumber)
while number != minNumber:
    sing = input('Введите знак > < ')
    if sing == '>':

        maxNumber = ((maxNumber - minNumber) / 2) + minNumber
        print(round(maxNumber))
    elif sing == '<':
        maxNumber = 50
        maxNumber = ((maxNumber - minNumber) / 2)+ minNumber
        print(round(maxNumber))
else:
    print('Победа')

# import random
#
# number = int(input('Введите число: '))
# minNumber = 0
# maxNumber = 100
# i = random.randint(minNumber, maxNumber)
# print(i)
# while number != i:
#     sing = input('Введите знак > < ')
#     if sing == '>':
#         minNumber = i
#     elif sing == '<':
#         maxNumber = i
#     i = random.randint(minNumber, maxNumber)
#     print(i)
# else:
#     print('Победа')
