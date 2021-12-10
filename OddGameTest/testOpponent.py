import unittest

from opponent import Opponent

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.o = Opponent()

    def tearDown(self):
        pass

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
        self.o.setBetCount()
        self.assertEqual(0 < self.o.getBetCount() <= self.o.getCount(), True)
        self.o.setBetCount()
        self.assertEqual(0 < self.o.getBetCount() <= self.o.getCount(), True)
        self.o.setBetCount()
        self.assertEqual(0 < self.o.getBetCount() <= self.o.getCount(), True)

        self.o.winMarble(4)
        self.o.setBetCount()
        self.assertEqual(0 < self.o.getBetCount() <= 6, True)
        self.o.setBetCount()
        self.assertEqual(0 < self.o.getBetCount() <= 6, True)
        self.o.setBetCount()
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


if __name__ == '__main__':
    unittest.main()

