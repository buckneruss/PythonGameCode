class Player(object):
    """Primary class that stores and calculates all Player info"""

    def __init__(self, NameOfClass):
        if ReadClassList(NameOfClass) is not None: # may need to change
            PlayerClass = ReadJSONList(NameOfClass)
            self.className = PlayerClass['ID'] # redundant?
            self.Stamina()
            self.Armor()
            self.HandSize()
            self.PlayerDeck()

        else:
            print(NameOfClass, "does not exist")

