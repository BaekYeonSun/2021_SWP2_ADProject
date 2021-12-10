import sys

from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

from player import Player
from opponent import Opponent
from showMarble import ShowMarble

from pygame import mixer

class OddGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # 레이아웃 사전 준비
        textList = ['남은 구슬 : ', '건 구슬 : ', '홀/짝 : ']
        oddList = ['홀', '짝']
        self.opponentShow = list(range(len(textList)))
        self.playerShow = list(range(len(textList)))
        # opponentShow[0]~[2]와 playerShow[0]~[2]는 각각 상대와 플레이어의 남은 구슬 개수, 건 구슬 개수, 홀/짝 이다.
        gameLayout = list(range(4))
        for i in range(len(gameLayout)):
            gameLayout[i] = QHBoxLayout()

        # 레이아웃 배치 시작
        gameName = QLabel('홀짝게임')  # 게임 제목
        font = gameName.font()
        font.setBold(True)
        font.setPointSize(font.pointSize() + 40)
        gameName.setFont(font)
        gameName.setAlignment(Qt.AlignCenter)

        opponentLabel = QLabel('상대')  # 아래가 상대의 상태임일 나타내주기 위한 라벨
        font = opponentLabel.font()
        font.setBold(True)
        font.setPointSize(font.pointSize() + 20)
        opponentLabel.setFont(font)
        opponentLabel.setAlignment(Qt.AlignCenter)

        for i in range(len(textList)):  # 상대의 구슬 상태 등을 표시
            opponentStatusLabel = QLabel(textList[i])
            gameLayout[0].addWidget(opponentStatusLabel)
            self.opponentShow[i]=QLineEdit()
            self.opponentShow[i].setReadOnly(True)
            self.opponentShow[i].setFixedWidth(50)
            gameLayout[0].addWidget(self.opponentShow[i])

        self.showMarblePlace = QLabel()  # 주먹 속 구슬을 보여줄 곳
        self.showMarblePlace.setAlignment(Qt.AlignCenter)
        self.showMarblePlace.resize(300,200)

        for i in range(len(textList)):  # 플레이어의 구슬 상태 등을 표시
            playerStatusLabel = QLabel(textList[i])
            gameLayout[1].addWidget(playerStatusLabel)
            self.playerShow[i]=QLineEdit()
            self.playerShow[i].setReadOnly(True)
            self.playerShow[i].setFixedWidth(50)
            gameLayout[1].addWidget(self.playerShow[i])

        for i in range(1,7):  # 플레이어가 구슬을 걸기 위한 버튼들
            Button = QPushButton()
            Button.setText(str(i))
            Button.clicked.connect(self.betCountClicked)
            Button.setFixedWidth(50)
            Button.setFixedHeight(50)
            gameLayout[2].addWidget(Button)

        for txt in oddList:  # 플레이어가 홀/짝을 고르기 위한 버튼들
            Button=QPushButton()
            Button.setText(txt)
            Button.clicked.connect(self.answerClicked)
            Button.setFixedWidth(170)
            Button.setFixedHeight(100)
            gameLayout[3].addWidget(Button)


        leftLayout = QVBoxLayout()  # 왼쪽 레이아웃
        leftLayout.addWidget(opponentLabel)
        for layout in gameLayout:
            if layout == gameLayout[1]:
                leftLayout.addWidget(self.showMarblePlace)
            leftLayout.addLayout(layout)

        self.log = QTextEdit()  # 게임 진행 로그
        self.log.setReadOnly(True)
        reset = QPushButton()  # 게임 초기화 버튼
        reset.setText("Reset")
        reset.clicked.connect(self.startGame)

        rightLayout = QVBoxLayout()  # 오른쪽 레이아웃
        rightLayout.addWidget(reset)
        rightLayout.addWidget(self.log)

        mainLayout = QGridLayout()  # 제목과 왼쪽, 오른쪽 레이아웃을 합침
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(gameName,0,0,1,2)
        mainLayout.addLayout(leftLayout,1,0)
        mainLayout.addLayout(rightLayout,1,1)

        self.setLayout(mainLayout)
        self.setWindowTitle('Odd Game')
        self.startGame()

    def startGame(self):  # 새 게임 시작
        self.ableToBet = False  # 구슬 걸기 버튼을 막 눌러서 생기는 오류 방지. True일 때만 버튼이 작동한다.
        self.ableToOdd = False  # 홀/짝 버튼을 막 눌러서 생기는 오류 방지. True일 때만 버튼이 작동한다.

        mixer.init()
        self.getMarbleSound = mixer.Sound("Sound/getMarble.mp3")  # 구슬 얻는 효과음
        self.getMarbleSound.set_volume(0.5)
        self.loseMarbleSound = mixer.Sound("Sound/loseMarble.mp3")  # 구슬 잃는 효과음
        self.loseMarbleSound.set_volume(0.5)
        self.winSound = mixer.Sound("Sound/win.mp3")  # 승리 효과음
        self.winSound.set_volume(0.4)
        self.loseSound = mixer.Sound("Sound/lose.mp3")  # 패배 효과음
        self.loseSound.set_volume(0.4)

        self.player = Player()
        self.opponent = Opponent()
        self.showMarble = ShowMarble()
        self.log.clear()

        self.player.decideTurn()  # 플레이어 턴 무작위 결정
        self.resetInterface()
        self.log.append("홀짝게임에 오신 걸 환영합니다.")
        self.runGame()

    def resetInterface(self):  # 남은 구슬 개수 갱신 및 입력칸을 빈칸으로 초기화
        self.showMarblePlace.setPixmap(QPixmap(self.showMarble.imageList[6]))
        self.opponentShow[0].setText(str(self.opponent.getCount()))
        self.opponentShow[1].setText('...')
        self.opponentShow[2].setText('...')
        self.playerShow[0].setText(str(self.player.getCount()))
        self.playerShow[1].setText('...')
        self.playerShow[2].setText('...')

    def runGame(self):  # 게임 진행
        if not self.player.checkEnd():
            if self.player.getTurn():  # 내 차례
                if self.playerShow[1].text() == '...':  # 플레이어가 구슬을 걸었는지 확인
                    self.sleep(1)
                    self.log.append("\n내 차례이다.")
                    self.sleep(1)
                    self.log.append("구슬 몇개를 걸까...")
                    self.ableToBet = True
                elif self.playerShow[2].text() == '...':  # 플레이어가 홀/짝을 정했는지 확인
                    self.sleep(1)
                    self.log.append("상대 주먹 속 구슬 개수가 홀수일까 짝수일까?")
                    self.ableToOdd = True
                else:  # 모든 입력이 끝나면
                    self.sleep(1)

                    self.opponent.setBetCount()
                    self.log.append("상대가 주먹을 연다.")
                    self.sleep(1)

                    self.showMarblePlace.setPixmap(QPixmap(self.showMarble.showMarble(self.opponent.getBetCount())))
                    if self.player.checkAnswerIsOdd() == (self.opponent.getBetCount() % 2 == 1):
                        self.log.append("이겼다! 구슬 "+str(self.player.getBetCount())+"개를 얻었다!")
                        self.player.winMarble(self.player.getBetCount())
                        self.opponent.loseMarble(self.player.getBetCount())
                        self.getMarbleSound.play()  # 구슬 얻는 효과음 재생
                    else:
                        self.log.append("졌다... 구슬 "+str(self.player.getBetCount())+"개를 잃었다...")
                        self.player.loseMarble(self.player.getBetCount())
                        self.opponent.winMarble(self.player.getBetCount())
                        self.loseMarbleSound.play()  # 구슬 잃는 효과음 재생
                    self.sleep(2)

                    self.player.switchTurn()
                    self.resetInterface()
                    self.runGame()

            else:  # 상대 차례
                if self.opponentShow[1].text() == '...':  # 상대가 구슬을 걸었는지 확인
                    self.sleep(1)
                    self.log.append("\n상대 차례이다.")
                    self.sleep(1)
                    self.opponent.setBetCount()
                    self.opponentShow[1].setText(str(self.opponent.getBetCount()))
                    self.log.append("상대가 구슬 " + str(self.opponent.getBetCount()) + "개 걸었다.")
                    self.sleep(1)
                    self.log.append("주먹에 구슬을 몇개 넣을까?")
                    self.ableToBet = True
                else:  # 모든 입력이 끝나면
                    self.showMarblePlace.setPixmap(QPixmap(self.showMarble.showMarble(self.player.getBetCount())))
                    self.sleep(1)

                    self.opponent.setAnswer()
                    self.opponentShow[2].setText(self.opponent.getAnswer())
                    self.log.append("상대가 "+self.opponent.getAnswer()+"을 골랐다!")
                    self.sleep(1)

                    if self.opponent.checkAnswerIsOdd() == (self.player.getBetCount() % 2 == 1):
                        self.log.append("졌다... 구슬 " + str(self.opponent.getBetCount()) + "개를 잃었다...")
                        self.player.loseMarble(self.opponent.getBetCount())
                        self.opponent.winMarble(self.opponent.getBetCount())
                        self.loseMarbleSound.play()  # 구슬 잃는 효과음 재생
                    else:
                        self.log.append("이겼다! 구슬 " + str(self.opponent.getBetCount()) + "개를 얻었다!")
                        self.player.winMarble(self.opponent.getBetCount())
                        self.opponent.loseMarble(self.opponent.getBetCount())
                        self.getMarbleSound.play()  # 구슬 얻는 효과음 재생
                    self.sleep(2)

                    self.player.switchTurn()
                    self.resetInterface()
                    self.runGame()
        else:  # 승부가 날 경우
            if self.player.getCount()>=20:
                self.log.append("*****    승리    *****")
                self.showMarblePlace.setPixmap(QPixmap(self.showMarble.showWin()))
                self.playerShow[0].setText("20")
                self.opponentShow[0].setText("0")
                self.winSound.play()  # 승리 효과음 재생
            elif self.player.getCount()<=0:
                self.log.append("=====    패배    =====")
                self.showMarblePlace.setPixmap(QPixmap(self.showMarble.showLose()))
                self.playerShow[0].setText("0")
                self.opponentShow[0].setText("20")
                self.loseSound.play()  # 패배 효과음 재생



    def sleep(self,n):  # PyQt에서는 작동하지 않는 time 모듈의 sleep 메소드를 대신함.
        QTest.qWait(n*1000)

    def betCountClicked(self):  # 구슬 걸기 버튼 클릭 시
        button = self.sender()
        if self.ableToBet == True:  # ableToBet이 True일 때만 작동
            if int(button.text())>self.player.getCount():
                self.log.append("구슬이 부족하다.")
            else:
                self.playerShow[1].setText(button.text())
                self.player.setBetCount(int(button.text()))
                self.log.append(str(self.player.getBetCount())+"개를 골랐다.")
                self.ableToBet = False
                self.runGame()

    def answerClicked(self):  # 홀/짝 버튼 클릭 시
        button = self.sender()
        if self.ableToOdd == True:  # ableToOdd가 True일 때만 작동
            self.playerShow[2].setText(button.text())
            self.player.setAnswer(button.text())
            self.log.append(self.player.getAnswer()+"을 골랐다.")
            self.ableToOdd = False
            self.runGame()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    game = OddGame()
    game.show()

    backGroundMusic = mixer.Sound("Sound/backgroundmusic.mp3")  # bgm 불러오기
    backGroundMusic.set_volume(0.3)
    backGroundMusic.play(-1)  # bgm 재생

    sys.exit(app.exec_())
