from marble import *
from showMarble import ShowMarble

def gameMain():
    player = Player()
    opponent = Opponent()
    showMarble = ShowMarble()

    while not player.checkEnd():
        print()
        if player.getTurn(): #내 차례
            print("구슬 몇개를 걸까... (현재 ", player.getCount(), "개 있다.)")
            try:
                display = int(input("입력 : "))
            except ValueError:
                print("숫자만 입력하시오.")
                continue
            if display > player.getCount():
                print("구슬이 부족하다...")
                continue
            elif display < 1:
                print("적어도 하나는 걸자.")
                continue
            player.setBetCount(display)

            opponent.setFistMarble()
            print("상대 주먹의 구슬 개수가 홀수일까...? 짝수일까...?")
            display = input("입력 (홀/짝) : ")
            if display != '홀' and display != '짝':
                print("홀이나 짝만 입력할 수 있다.")
                continue
            player.setAnswer(display)

            display = showMarble.showMarble(opponent.getBetCount())
            print(display)
            if player.checkAnswerIsOdd() == (opponent.getBetCount()%2 == 1):
                print("이겼다! 구슬 ", player.getBetCount(), "개를 얻었다!")
                player.winMarble(player.getBetCount())
                opponent.loseMarble(player.getBetCount())
            else:
                print("졌다... 구슬 ", player.getBetCount(), "개를 잃었다...")
                player.loseMarble(player.getBetCount())
                opponent.winMarble(player.getBetCount())


        else: #상대 차례
            print("주먹에 구슬 몇개를 넣을까... (현재 ", player.getCount(), "개 있다.)")
            try:
                display = int(input("입력 (1~6) : "))
            except ValueError:
                print("숫자만 입력하시오.")
                continue
            if display > 6 or display < 1:
                print("1개부터 6개만 넣을 수 있다!")
                continue
            elif display > player.getCount():
                print("구슬이 부족하다...")
                continue
            player.setBetCount(display)

            display = showMarble.showMarble(player.getBetCount())
            print(display)

            opponent.setBetCount()
            opponent.setAnswer()
            print("상대가 구슬 ", opponent.getBetCount(), "개를 걸고 \'", opponent.getAnswer(), "\'을/를 골랐다.")

            if opponent.checkAnswerIsOdd() == (player.getBetCount()%2 == 1):
                print("졌다... 구슬 ", opponent.getBetCount(), "개를 잃었다...")
                player.loseMarble(opponent.getBetCount())
                opponent.winMarble(opponent.getBetCount())
            else:
                print("이겼다! 구슬 ", opponent.getBetCount(), "개를 얻었다!")
                player.winMarble(opponent.getBetCount())
                opponent.loseMarble(opponent.getBetCount())

        player.switchTurn()

        if player.checkEnd():
            if player.getCount() >= 20:
                print("*****   승리   *****")
            elif player.getCount() <=0:
                print("=====   패배   =====")



if __name__ == '__main__':
    gameMain()