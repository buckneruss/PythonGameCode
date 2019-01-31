"""
Controls which player the enemy will move and attack during their turn
"""

from random import randrange


class TargetNearest(object):
    """
    Targeting used by Grunts
    Targets the nearest Player
    """
    def __init__(self, grunt, player_list):
        self.grunt = grunt
        self.player_list = player_list

    def find_nearest_player(self):  # Move into separate module?
        nearest_player = []
        shortest_distance = None
        for player in self.player_list:
            if shortest_distance is None:
                nearest_player.append(player)
                shortest_distance = self.__get_distance(self.grunt, player)
            elif shortest_distance > self.__get_distance(self.grunt, player):
                nearest_player.clear()
                nearest_player.append(player)
                shortest_distance = nearest_player.append(player)
            elif shortest_distance == self.__get_distance(self.grunt, player):
                nearest_player.append(player)

        if len(nearest_player) > 1:
            i = randrange(len(nearest_player))
        else:
            i = 1
        target = nearest_player[i]
        return target

    def __get_distance(self, enemy, player):
        x = abs(enemy.Position[0] - player.Position[0])
        y = abs(enemy.Position[1] - player.Position[1])
        return x + y


class TargetAT(object):
    """
    Special targeting that only Elites use.
    Creates an Aggression Token and "gives" it to the Player which
    fulfills its targeting restriction.
    If an Elite already has an Aggression Token in effect, it uses it instead
    of creating a new one.
    """
    def __init__(self, enemy, player_list):
        self.enemy = enemy
        self.player_list = player_list

    def find_AT_target(self):
        if self.enemy.AT is None:
            self.__create_AT()
        target = self.enemy.AT.player
        return target

    def __create_AT(self):
        player = self.__elite_targeting()
        self.enemy.AT = AggressionToken(self.enemy, player)

    # def __find_player_with_stat(self, stat, value):  # make dynamic
    #     target_list = []
    #     for player in self.player_list:
    #         pass
    #     return target_list[0]

    def __elite_targeting(self):  # redo later
        role = self.enemy.Role_Name

        if role == 'Champion':
            valid_target = []
            lowest_armor = None
            for player in self.player_list:
                if lowest_armor is None:
                    valid_target.append(player)
                    lowest_armor = player.Armor.value
                elif lowest_armor > player.Armor.value:
                    valid_target.clear()
                    valid_target.append(player)
                    lowest_armor = player.Armor.value
                elif lowest_armor == player.Armor.value:
                    valid_target.append(player)
            if len(valid_target) == 1:
                return valid_target[0]
            else:
                shortest_distance = None
                closest_target = valid_target
                for player in closest_target:
                    if shortest_distance is None:
                        closest_target.append(player)
                        shortest_distance = self.__get_distance(self.enemy, player)
                    elif shortest_distance > self.__get_distance(self.enemy, player):
                        closest_target.clear()
                        closest_target.append(player)
                        shortest_distance = self.__get_distance(self.enemy, player)
                    elif shortest_distance == self.__get_distance(self.enemy, player):
                        closest_target.append(player)
                if len(closest_target) == 1:
                    return closest_target[0]
                else:
                    i = randrange(len(closest_target))
                    return closest_target[i]

        elif role == 'Caster':
            valid_target = []
            highest_armor = None
            for player in self.player_list:
                if highest_armor is None:
                    highest_armor = player.Armor.value
                elif highest_armor < player.Armor.value:
                    valid_target.clear()
                    valid_target.append(player)
                    highest_armor = player.Armor.value
                elif highest_armor == player.Armor.value:
                    valid_target.append(player)
            if len(valid_target) == 1:
                return valid_target[0]
            else:
                shortest_distance = None
                closest_target = valid_target
                for player in closest_target:
                    if shortest_distance is None:
                        shortest_distance = self.__get_distance(self.enemy, player)
                    elif shortest_distance > self.__get_distance(self.enemy, player):
                        closest_target.clear()
                        closest_target.append(player)
                        shortest_distance = self.__get_distance(self.enemy, player)
                    elif shortest_distance == self.__get_distance(self.enemy, player):
                        closest_target.append(player)
                if len(closest_target) == 1:
                    return closest_target[0]
                else:
                    i = randrange(len(closest_target))
                    return closest_target[i]

    def __get_distance(self, enemy, player):
        x = abs(enemy.Position[0] - player.Position[0])
        y = abs(enemy.Position[1] - player.Position[1])
        return x + y


class AggressionToken(object):
    """
    Object which links an Elite to a Player based on a predefined condition.
    A Player can have any number of Aggression Tokens, but an Elite can only
    have one Aggression Token at a time.
    Aggression Tokens can be moved from Player to Player
    """
    def __init__(self, elite, player):
        self.elite = elite  # Source of the Aggression Token, shouldn't change
        self.player = player  # Target of the Token, can easily change

    def get_player_location(self):
        return self.player.Position
