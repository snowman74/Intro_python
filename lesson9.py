import random


class DurakGame:

    def __init__(self):
        self.all_cards = [(6, 'Черви'), (7, 'Черви'), (8, 'Черви'), (9, 'Черви'), (10, 'Черви'), (11, 'Черви'), (12, 'Черви'), (13, 'Черви'), (14, 'Черви'),
                          (6, 'Буби'), (7, 'Буби'), (8, 'Буби'), (9, 'Буби'), (10, 'Буби'), (11, 'Буби'), (12, 'Буби'), (13, 'Буби'), (14, 'Буби'),
                          (6, 'Крести'), (7, 'Крести'), (8, 'Крести'), (9, 'Крести'), (10, 'Крести'), (11, 'Крести'), (12, 'Крести'), (13, 'Крести'), (14, 'Крести'),
                          (6, 'Пики'), (7, 'Пики'), (8, 'Пики'), (9, 'Пики'), (10, 'Пики'), (11, 'Пики'), (12, 'Пики'), (13, 'Пики'), (14, 'Пики')]
        self.player_cards = []
        self.pc_cards = []
        self.table = []

    def razdacha(self):
        for i in range(6):
            self.player_cards.append(self.all_cards.pop(random.randint(0, len(self.all_cards) - 1)))
            self.pc_cards.append(self.all_cards.pop(random.randint(0, len(self.all_cards) - 1)))
        self.player_cards.sort(key=lambda i: i[0], reverse=False)
        self.pc_cards.sort(key=lambda i: i[0], reverse=False)

    def turn_player(self):
        print(f'У вас на руках: {self.player_cards}')
        i = int(input('Введите индекс карты, которой вы хотите сходить: '))
        self.table.append(self.player_cards.pop(i))
        print(f'На столе сейчас: {self.table}')
        print(f'У вас на руках: {player_cards}')

    def turn_pc(self):
        i = 0
        while True:
            try:
                if self.pc_cards[i][0] > self.table[0][0] and self.pc_cards[i][1] == self.table[0][1]:
                    print(f'Компьютер отбивает {self.pc_cards[i]}')
                    self.pc_cards.pop(i)
                    self.table.clear()
                    break
                else:
                    i += 1
            except IndexError:
                print('Компьютер не смог отбить')
                self.pc_cards.append(self.table[0])
                break

        print(f"Расклад такой:\n",
              f"У компьютера на руках {pc_cards}\n",
              f'У вас на руках {player_cards}')



