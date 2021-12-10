class ShowMarble:
    def __init__(self):

        self.imageList = [
            "Image/oneMarble.jpg",
            "Image/twoMarble.jpg",
            "Image/threeMarble.jpg",
            "Image/fourMarble.jpg",
            "Image/fiveMarble.jpg",
            "Image/sixMarble.jpg",
            "Image/noMarble.jpg",
            "Image/win.jpg",
            "Image/lose.jpg",
        ]  # 화면에 표시 할 구슬



    def showMarble(self, count):
        return self.imageList[count-1]
    def showBlank(self):
        return self.imageList[6]
    def showWin(self):
        return self.imageList[7]
    def showLose(self):
        return self.imageList[8]