import random # ! Do NOT modify this line !

MIN = 1
MAX = 6

class Dice:
    def __init__(self):
        self.top_face = 1

    def set_top_face(self, num):
        if type(num) != int:
            return False

        if num >= MIN  and num <= MAX:
            self.top_face = num 
            return True
        return False
    
    def roll_dice(self):
        num = random.randint(MIN, MAX) # ! Do NOT modify this line !
        self.set_top_face(num)
        return num

    def __str__(self):
        return f"{self.top_face}"