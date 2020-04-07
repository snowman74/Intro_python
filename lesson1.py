# bones

from random import randint

game = input('Введите 1, если хотите сыграть, либо нажмите любую клавишу')
while game == '1':
    step_pc = randint(1, 6)
    print('Компьютер выкинул', step_pc)
    input('Нажмите Enter, чтобы бросить кубик...')
    step_player = randint(1,6)
    print('Вам выпало', step_player)
    if step_player < step_pc:
        print('Вы проиграли')
    elif step_pc < step_player:
        print('Вы выиграли')
    else:
        print('Ничья')
    game = input('Введите 1, если хотите сыграть, либо нажмите любую клавишу')
print('Всего хорошего!')