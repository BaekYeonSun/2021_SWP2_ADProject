import random
from marble import Marble

class Player(Marble):

    def __init__(self):
        super().__init__()
        self.myTurn = True

    def checkEnd(self):
        if self.getCount() <= 0 or self.getCount() >= 20:
            return True
        else:
            return False

    def setAnswer(self, Odd):
        self.answer = Odd

    def setBetCount(self, num):
        self.betCount = num

    def getTurn(self):
        return self.myTurn

    def switchTurn(self):
        if self.getTurn():
            self.myTurn = False
        else:
            self.myTurn = True

    def decideTurn(self):  # 턴 랜덤 결정
        i = random.randrange(2)
        if i == 0:
            self.myTurn = True
        else:
            self.myTurn = False
