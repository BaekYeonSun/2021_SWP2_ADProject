import unittest

from player import Player

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.p = Player()

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



if __name__ == '__main__':
    unittest.main()

