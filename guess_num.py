from random import randint


pc_num = randint(1, 100)
print('Угадай число от 1 до 100')
while True:
    user_num = int(input('Введите число: '))
    if user_num > pc_num:
        print('Ваше число больше загаданного. Попробуйте снова.')
    elif user_num < pc_num:
        print('Ваше число меньше загаданного. Попробуйте снова.')
    elif user_num == pc_num:
        break
print('Победа. Вы угадали загаданное число.')