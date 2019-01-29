from UnitStat import *


class Enemy(object):
    """
    Primary class that stores and calculates all Player info
    """

    def __init__(self, race, role, number):
        self.race_info = race
        self.role_info = role
        self.Race_Name = self.race_info['ID']
        self.Role_Name = self.race_info['ID']
        self.Enemy_Number = number
        self.Position = None
        self.Health_Points = self.race_info['Base_Health'] + self.role_info['Bonus_Health']
        self.Stamina = Stamina(self.race_info['Stamina_Pool'] + self.role_info['Bonus_SP'])
        self.Weapon_Damage = StatTracker(self.role_info['Bonus_Damage'])
        self.Armor = StatTracker(self.race_info['Base_Armor'] + self.role_info['Bonus_Armor'])
        self.Bonus_Range = StatTracker()
        self.Equipment = []  # Starting Equipment
        # self.Passive

    def turn_beginning(self):
        self.Stamina.reset_stamina_points()
        # mulligan phase
        # upkeep

    def print_info(self):  # fix: prints None at end?
        print('\n' + self.Race_Name, self.Role_Name)
        print('Position:', self.Position)
        print('Health:', self.Health_Points)
        print('Stamina Pool:', self.Stamina.get_pool_size())
        print('Remaining Stamina:', self.Stamina.get_stamina_points())
        print('Weapon Damage:', self.Weapon_Damage.value)
        print('Bonus Range:', self.Bonus_Range.value)
        print('Armor:', self.Armor.value)

    def get_enemy_name(self):
        return self.Race_Name + ' ' + self.Role_Name

    # Equipment Stuff
    def get_equipped_list(self):
        return self.Equipment

    def get_equipped_item(self, item):
        for i in self.Equipment:
            if i.Name == item:
                return i

    def add_equipment(self, item):
        self.Equipment.append(item)
        if 'Damage' in item.Equipment_Stats:
            self.Weapon_Damage.add_effect(item.Name, item.Equipment_Stats['Damage'])
        if 'Armor' in item.Equipment_Stats:
            self.Armor.add_effect(item.Name, item.Equipment_Stats['Armor'])
        if 'Range' in item.Equipment_Stats:
            self.Bonus_Range.add_effect(item.Name, item.Equipment_Stats['Range'])
        if 'Stamina' in item.Equipment_Stats:
            self.Stamina.add_pool_effect(item.Name, item.Equipment_Stats['Stamina'])
