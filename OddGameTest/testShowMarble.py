import unittest

from showMarble import ShowMarble

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.s = ShowMarble()

    def tearDown(self):
        pass

    def testShow(self):
        self.assertEqual(self.s.showMarble(1), "Image/oneMarble.jpg")
        self.assertEqual(self.s.showMarble(2), "Image/twoMarble.jpg")
        self.assertEqual(self.s.showMarble(3), "Image/threeMarble.jpg")
        self.assertEqual(self.s.showMarble(4), "Image/fourMarble.jpg")
        self.assertEqual(self.s.showMarble(5), "Image/fiveMarble.jpg")
        self.assertEqual(self.s.showMarble(6), "Image/sixMarble.jpg")
        self.assertEqual(self.s.showBlank(), "Image/noMarble.jpg")
        self.assertEqual(self.s.showWin(), "Image/win.jpg")
        self.assertEqual(self.s.showLose(), "Image/lose.jpg")

if __name__ == '__main__':
    unittest.main()

