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

    def checkAnswerIsOdd(self):  # 답이 홀/짝인지에 따라 boolean을 내보냄. getAnswer 메소드와 혼동 주의
        if self.answer == '홀':
            return True
        elif self.answer == '짝':
            return False

    def getAnswer(self):  # 답 그 자체를 리턴함. checkAnswerIsOdd 메소드와 혼동 주의.
        return self.answer

    def getBetCount(self):
        return self.betCount

    def getCount(self):
        return self.count
