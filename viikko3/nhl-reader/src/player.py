class Player:
    def __init__(self, name, goals, assists, nationality):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.nationality = nationality

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {str(self.goals):2} + {str(self.assists):2} = {self.points}"
