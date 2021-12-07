import unittest

from marble import *
from showMarble import ShowMarble

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.p = Player()
        self.o = Opponent()
        self.s = ShowMarble()

    def tearDown(self):
        pass

    def testPlayer(self):
        self.assertEqual(self.p.getCount(), 10)
        self.p.loseMarble(2)
        self.assertEqual(self.p.getCount(), 8)
        self.p.winMarble(5)
        self.assertEqual(self.p.getCount(), 13)

        self.p.setBetCount(7)
        self.assertEqual(self.p.getBetCount(), 7)

        self.assertEqual(self.p.getTurn(), True)
        self.p.switchTurn()
        self.assertEqual(self.p.getTurn(), False)

        self.p.setAnswer("홀")
        self.assertEqual(self.p.getAnswer(), "홀")
        self.assertEqual(self.p.checkAnswerIsOdd(), True)
        self.p.setAnswer("짝")
        self.assertEqual(self.p.getAnswer(), "짝")
        self.assertEqual(self.p.checkAnswerIsOdd(), False)

        self.p.winMarble(7)
        self.assertEqual(self.p.checkEnd(), True)
        self.p.winMarble(10000)
        self.assertEqual(self.p.checkEnd(), True)
        self.p.loseMarble(10007)
        self.assertEqual(self.p.checkEnd(), False)
        self.p.loseMarble(4000)
        self.assertEqual(self.p.checkEnd(), True)

    def testOpponent(self):
        self.assertEqual(self.o.getCount(), 10)
        self.o.loseMarble(2)
        self.assertEqual(self.o.getCount(), 8)
        self.o.winMarble(5)
        self.assertEqual(self.o.getCount(), 13)

        self.o.setBetCount()
        self.assertEqual(0 < self.o.getBetCount() <= self.o.getCount(), True)
        self.o.setBetCount()
        self.assertEqual(0 < self.o.getBetCount() <= self.o.getCount(), True)
        self.o.setBetCount()
        self.assertEqual(0 < self.o.getBetCount() <= self.o.getCount(), True)

        self.o.loseMarble(9)
        self.o.setFistMarble()
        self.assertEqual(0 < self.o.getBetCount() <= self.o.getCount(), True)
        self.o.setFistMarble()
        self.assertEqual(0 < self.o.getBetCount() <= self.o.getCount(), True)
        self.o.setFistMarble()
        self.assertEqual(0 < self.o.getBetCount() <= self.o.getCount(), True)

        self.o.winMarble(4)
        self.o.setFistMarble()
        self.assertEqual(0 < self.o.getBetCount() <= 6, True)
        self.o.setFistMarble()
        self.assertEqual(0 < self.o.getBetCount() <= 6, True)
        self.o.setFistMarble()
        self.assertEqual(0 < self.o.getBetCount() <= 6, True)

        self.o.setAnswer()
        print(self.o.getAnswer())
        print(self.o.checkAnswerIsOdd())
        self.o.setAnswer()
        print(self.o.getAnswer())
        print(self.o.checkAnswerIsOdd())
        self.o.setAnswer()
        print(self.o.getAnswer())
        print(self.o.checkAnswerIsOdd())
        self.o.setAnswer()
        print(self.o.getAnswer())
        print(self.o.checkAnswerIsOdd())
        self.o.setAnswer()
        print(self.o.getAnswer())
        print(self.o.checkAnswerIsOdd())

    def testShow(self):
        self.assertEqual(self.s.showMarble(1), 'o')
        self.assertEqual(self.s.showMarble(2), 'oo')
        self.assertEqual(self.s.showMarble(3), 'ooo')
        self.assertEqual(self.s.showMarble(4), 'oooo')
        self.assertEqual(self.s.showMarble(5), 'ooooo')
        self.assertEqual(self.s.showMarble(6), 'oooooo')


if __name__ == '__main__':
    unittest.main()

