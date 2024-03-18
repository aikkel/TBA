class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.skills = {}
        self.stamina = 100
        self.luck = 10