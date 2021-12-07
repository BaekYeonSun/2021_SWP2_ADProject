import random

class Marble:

    def __init__(self):
        self.count = 10
        self.betCount = 0
        self.isOdd = False
        self.answer = ''

    def loseMarble(self, count):
        self.count -= count

    def winMarble(self, count):
        self.count += count

    def checkAnswerIsOdd(self):
        if self.answer == '홀':
            return True
        elif self.answer == '짝':
            return False

    def getAnswer(self):
        return self.answer

    def getBetCount(self):
        return self.betCount

    def getCount(self):
        return self.count


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
    def decideTurn(self):
        i = random.randrange(1, 3)
        if i == 1:
            self.myTurn = True
        else:
            self.myTurn = False

class Opponent(Marble):
    def __init__(self):
        super().__init__()
        self.difficulty = 'human'

    def setBetCount(self):
        if self.getCount()<6:
            self.betCount = random.randrange(1, self.getCount()+1)
        else:
            self.betCount = random.randrange(1,7)

    def setAnswer(self):
        i = random.randrange(1,3)
        if i == 1:
            self.answer = '홀'
        else:
            self.answer = '짝'