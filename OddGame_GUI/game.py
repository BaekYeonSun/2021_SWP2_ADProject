
from PyQt5.QtTest import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QPushButton, QLabel

from marble import *
from showMarble import ShowMarble

class OddGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        #display set
        self.gameName = QLabel('홀짝게임')
        font = self.gameName.font()
        font.setBold(True)
        font.setPointSize(font.pointSize() + 40)
        self.gameName.setFont(font)
        self.gameName.setAlignment(Qt.AlignCenter)

        self.opponentLabel = QLabel('상대')
        font = self.opponentLabel.font()
        font.setBold(True)
        font.setPointSize(font.pointSize() + 20)
        self.opponentLabel.setFont(font)
        self.opponentLabel.setAlignment(Qt.AlignCenter)

        opponentLayout = QGridLayout()

        self.opponentCountLabel = QLabel('남은 구슬 : ')
        self.opponentCountShow = QLineEdit()
        self.opponentCountShow.setReadOnly(True)
        self.opponentCountShow.setFixedWidth(50)
        self.opponentBetCountLabel = QLabel('건 구슬 : ')
        self.opponentBetCountShow = QLineEdit()
        self.opponentBetCountShow.setReadOnly(True)
        self.opponentBetCountShow.setFixedWidth(50)
        self.opponentOddLabel = QLabel('홀/짝 : ')
        self.opponentOddShow = QLineEdit()
        self.opponentOddShow.setReadOnly(True)
        self.opponentOddShow.setFixedWidth(50)
        opponentLayout.addWidget(self.opponentCountLabel,0,0)
        opponentLayout.addWidget(self.opponentCountShow,0,1)
        opponentLayout.addWidget(self.opponentBetCountLabel,0,2)
        opponentLayout.addWidget(self.opponentBetCountShow,0,3)
        opponentLayout.addWidget(self.opponentOddLabel,0,4)
        opponentLayout.addWidget(self.opponentOddShow,0,5)

        self.showMarblePlace = QTextEdit()
        self.showMarblePlace.setReadOnly(True)
        self.showMarblePlace.setAlignment(Qt.AlignVCenter)
        font = self.showMarblePlace.font()
        font.setPointSize(font.pointSize() + 50)
        self.showMarblePlace.setFont(font)

        myLayout = QGridLayout()
        self.myCountLabel = QLabel('남은 구슬 : ')
        self.myCountShow = QLineEdit()
        self.myCountShow.setReadOnly(True)
        self.myCountShow.setFixedWidth(50)
        self.myBetCountLabel = QLabel('건 구슬 : ')
        self.myBetCountShow = QLineEdit()
        self.myBetCountShow.setReadOnly(True)
        self.myBetCountShow.setFixedWidth(50)
        self.myOddLabel = QLabel('홀/짝 : ')
        self.myOddShow = QLineEdit()
        self.myOddShow.setReadOnly(True)
        self.myOddShow.setFixedWidth(50)
        myLayout.addWidget(self.myCountLabel,0,0)
        myLayout.addWidget(self.myCountShow,0,1)
        myLayout.addWidget(self.myBetCountLabel,0,2)
        myLayout.addWidget(self.myBetCountShow,0,3)
        myLayout.addWidget(self.myOddLabel,0,4)
        myLayout.addWidget(self.myOddShow,0,5)

        betButtonLayout = QGridLayout()
        for i in range(1,7):
            Button = QPushButton()
            Button.setText(str(i))
            Button.clicked.connect(self.betCountClicked)
            Button.setMinimumSize(50,50)
            Button.setMaximumSize(50, 50)
            betButtonLayout.addWidget(Button,0,i-1)

        oddButtonLayout = QGridLayout()
        self.isOddButton = QPushButton()
        self.isOddButton.setText("홀")
        self.isOddButton.clicked.connect(self.answerClicked)
        self.isOddButton.setMinimumSize(170,100)
        self.isOddButton.setMaximumSize(170,100)
        self.isNotOddButton = QPushButton()
        self.isNotOddButton.setText("짝")
        self.isNotOddButton.clicked.connect(self.answerClicked)
        self.isNotOddButton.setMinimumSize(170, 100)
        self.isNotOddButton.setMaximumSize(170, 100)
        oddButtonLayout.addWidget(self.isOddButton,0,0)
        oddButtonLayout.addWidget(self.isNotOddButton,0,1)

        leftLayout = QGridLayout()
        leftLayout.addWidget(self.opponentLabel,0,0)
        leftLayout.addLayout(opponentLayout,1,0)
        leftLayout.addWidget(self.showMarblePlace,2,0)
        leftLayout.addLayout(myLayout,3,0)
        leftLayout.addLayout(betButtonLayout,4,0)
        leftLayout.addLayout(oddButtonLayout,5,0)

        self.log = QTextEdit()
        self.log.setReadOnly(True)

        self.reset = QPushButton()
        self.reset.setText("Reset")
        self.reset.clicked.connect(self.startGame)

        rightLayout = QGridLayout()
        rightLayout.addWidget(self.reset,0,0)
        rightLayout.addWidget(self.log,1,0)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.gameName,0,0,1,2)
        mainLayout.addLayout(leftLayout,1,0)
        mainLayout.addLayout(rightLayout,1,1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Odd Game')

        self.startGame()

    def startGame(self):
        self.ableToBet = False
        self.ableToOdd = False
        self.player = Player()
        self.opponent = Opponent()
        self.showMarble = ShowMarble()
        self.log.clear()

        self.player.decideTurn()
        self.resetInterface()
        self.log.append("홀짝게임에 오신 걸 환영합니다.")
        self.runGame()

    def resetInterface(self):
        self.showMarblePlace.setPlaceholderText(" ")
        self.opponentCountShow.setText(str(self.opponent.getCount()))
        self.opponentBetCountShow.setText('...')
        self.opponentOddShow.setText('...')
        self.myCountShow.setText(str(self.player.getCount()))
        self.myBetCountShow.setText('...')
        self.myOddShow.setText('...')

    def runGame(self):
        if not self.player.checkEnd():
            if self.player.getTurn(): #내 차례
                if self.myBetCountShow.text() == '...' and self.ableToBet == False:
                    self.sleep(1)
                    self.log.append("\n내 차례이다.")
                    self.sleep(1)
                    self.log.append("구슬 몇개를 걸까...")
                    self.ableToBet = True
                elif self.myBetCountShow.text() != '...' and self.myOddShow.text() == '...' and self.ableToOdd == False:
                    self.sleep(1)
                    self.log.append("상대 주먹 속 구슬 개수가 홀수일까 짝수일까?")
                    self.ableToOdd = True
                elif self.myBetCountShow.text() != ',,,' and self.myOddShow.text() != '...':
                    self.sleep(1)
                    self.opponent.setBetCount()
                    self.log.append("상대가 주먹을 연다.")
                    self.sleep(1)
                    self.showMarblePlace.setPlaceholderText(self.showMarble.showMarble(self.opponent.getBetCount()))
                    if self.player.checkAnswerIsOdd() == (self.opponent.getBetCount() % 2 == 1):
                        self.log.append("이겼다! 구슬 "+str(self.player.getBetCount())+"개를 얻었다!")
                        self.player.winMarble(self.player.getBetCount())
                        self.opponent.loseMarble(self.player.getBetCount())
                    else:
                        self.log.append("졌다... 구슬 "+str(self.player.getBetCount())+"개를 잃었다...")
                        self.player.loseMarble(self.player.getBetCount())
                        self.opponent.winMarble(self.player.getBetCount())
                    self.sleep(2)
                    self.player.switchTurn()
                    self.resetInterface()
                    self.runGame()
            else: #상대 차례

                if self.opponentBetCountShow.text() == '...':
                    self.sleep(1)
                    self.log.append("\n상대 차례이다.")
                    self.sleep(1)
                    self.opponent.setBetCount()
                    self.opponentBetCountShow.setText(str(self.opponent.getBetCount()))
                    self.log.append("상대가 구슬 " + str(self.opponent.getBetCount()) + "개 걸었다.")
                    self.sleep(1)
                    self.log.append("주먹에 구슬을 몇개 넣을까?")
                    self.ableToBet = True
                elif self.myBetCountShow != '...':
                    self.showMarblePlace.setPlaceholderText(self.showMarble.showMarble(self.player.getBetCount()))
                    self.sleep(1)
                    self.opponent.setAnswer()
                    self.opponentOddShow.setText(self.opponent.getAnswer())
                    self.log.append("상대가 "+self.opponent.getAnswer()+"을 골랐다!")
                    self.sleep(1)
                    if self.opponent.checkAnswerIsOdd() == (self.player.getBetCount() % 2 == 1):
                        self.log.append("졌다... 구슬 " + str(self.opponent.getBetCount()) + "개를 잃었다...")
                        self.player.loseMarble(self.opponent.getBetCount())
                        self.opponent.winMarble(self.opponent.getBetCount())
                    else:
                        self.log.append("이겼다! 구슬 " + str(self.opponent.getBetCount()) + "개를 얻었다!")
                        self.player.winMarble(self.opponent.getBetCount())
                        self.opponent.loseMarble(self.opponent.getBetCount())
                    self.sleep(2)
                    self.player.switchTurn()
                    self.resetInterface()
                    self.runGame()
        else:
            if self.player.getCount()>=20:
                self.log.append("*****    승리    *****")
                self.showMarblePlace.setPlaceholderText("You Win!")
                self.myCountShow.setText("20")
                self.opponentCountShow.setText("0")
            elif self.player.getCount()<=0:
                self.log.append("=====    패배    =====")
                self.showMarblePlace.setPlaceholderText("You Lose...")
                self.myCountShow.setText("0")
                self.opponentCountShow.setText("20")



    def sleep(self,n):
        QTest.qWait(n*1000)

    def betCountClicked(self):
        button = self.sender()
        if self.ableToBet == True:
            if int(button.text())>self.player.getCount():
                self.log.append("구슬이 부족하다.")
            else:
                self.myBetCountShow.setText(button.text())
                self.player.setBetCount(int(button.text()))
                self.log.append(str(self.player.getBetCount())+"개를 골랐다.")
                self.ableToBet = False
                self.runGame()

    def answerClicked(self):
        button = self.sender()
        if self.ableToOdd == True:
            self.myOddShow.setText(button.text())
            self.player.setAnswer(button.text())
            self.log.append(self.player.getAnswer()+"을 골랐다.")
            self.ableToOdd = False
            self.runGame()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    game = OddGame()
    game.show()
    sys.exit(app.exec_())