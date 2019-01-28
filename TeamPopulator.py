from ReadGameData import SubListManager
from Player import Player

"""
Module that asks the Player to enter their name, then select which class they would
    like to play, then creates a Player object with the proper info.
"""


class TeamMaker(object):
    def __init__(self, c, e):
        self.class_list = SubListManager(c)
        self.equipment_list = SubListManager(e)
        self.player_list = []

    def team_init(self):
        global value  # needed for checking for the proper number of players
        value = True
        while value:
            try:
                v = int(input('\n' + 'Enter number of Players (1-4): '))
                if 0 < v <= 4:
                    value = False
                else:
                    print(v, 'is not a valid number')
            except ValueError:
                print('Invalid input, try again')
            else:
                break

        for i in range(v):
            name = input('\n' + 'Enter Player Name: ')
            selected_class = self.__select_class()
            class_info = self.class_list.get_item(selected_class)
            player = Player(class_info, name)
            # give player starting equipment
            # give player starting deck
            self.player_list.append(player)
        return self.player_list

    def __select_class(self):
        item_list = self.class_list.get_list()
        print('\n' + 'Select Class:')
        for i, item in enumerate(item_list):
            print(i, item['ID'], sep=': ')
        while True:
            try:
                v = int(input('Enter digit of class: '))
            except ValueError:
                print('Invalid input, try again', '\n')
            else:
                break

        selection = item_list[v]
        return selection['ID']
