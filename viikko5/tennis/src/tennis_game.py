class TennisGame:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return TennisGame.get_deuce_name(self.player1_score)
        
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return TennisGame.get_advantage_name(self.player1_score, self.player2_score)

        else:
            return TennisGame.get_score_name(self.player1_score) + "-" + TennisGame.get_score_name(self.player2_score)
    
    @staticmethod
    def get_advantage_name(p1_score, p2_score):
        if(p1_score < p2_score):
            if(p2_score - p1_score == 1):
                return "Advantage player2"
            else:
                return "Win for player2"
        else:
            if(p1_score - p2_score == 1):
                return "Advantage player1"
            else:
                return "Win for player1"

    @staticmethod
    def get_deuce_name(x):
        deuce_name = TennisGame.get_score_name(x)

        if len(deuce_name) == 0:
            return "Deuce"

        return deuce_name + "-All"

    @staticmethod
    def get_score_name(x):
        if x == 0:
            return "Love"
        elif x == 1:
            return "Fifteen"
        elif x == 2:
            return "Thirty"
        elif x == 3:    
            return "Forty"
        else:
            return ""
