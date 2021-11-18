class Player:
    def __init__(self, name, goals, assists):
        self.name = name
        self.goals = goals
        self.assists = assists

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name} {self.goals} + {self.assists} = {self.points}"

