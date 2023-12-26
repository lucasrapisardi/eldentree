class Player:
    level = 1

    def __init__(self, name):
        self.name = name
        # self.race = race
        # self.clas = clas
        # self.background = background

    def __str__(self):
        f"""{self.name} is a {self.clas} of the race {self.race}"""

    
        
