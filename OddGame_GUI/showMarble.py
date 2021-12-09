class ShowMarble:
    def __init__(self):
        self.marbleList = [
            'o',
            'oo',
            'ooo',
            'oooo',
            'ooooo',
            'oooooo',
        ]  # 화면에 표시 할 구슬

    def showMarble(self, count):
        return self.marbleList[count-1]