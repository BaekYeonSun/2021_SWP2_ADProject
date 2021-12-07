class ShowMarble:
    def __init__(self):
        self.marbleList = [
            'o',
            'oo',
            'ooo',
            'oooo',
            'ooooo',
            'oooooo',
        ]

    def showMarble(self, count):
        return self.marbleList[count-1]