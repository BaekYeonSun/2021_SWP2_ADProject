import random
from marble import Marble

class Opponent(Marble):
    def __init__(self):
        super().__init__()
        self.difficulty = 'human'

    def setBetCount(self):  # 구슬 개수 랜덤 결정
        if self.getCount() < 6:
            self.betCount = random.randrange(1, self.getCount() + 1)
        else:
            self.betCount = random.randrange(1, 7)

    def setAnswer(self):  # 홀/짝 랜덤 결정
        i = random.randrange(2)
        if i == 0:
            self.answer = '홀'
        else:
            self.answer = '짝'