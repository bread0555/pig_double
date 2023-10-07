class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


    def roll_dice(self, ls_dice):
        N = len(ls_dice)
        i = 0
        while i < N:
            ls_dice[i].roll_dice()
            i += 1


    def update_score(self, temp):
        if type(temp) == int and temp >= 0: # validity check
            self.score += temp
    
    def __str__(self):
        return f"{self.name}"