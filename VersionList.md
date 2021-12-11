# 업데이트 내역
-----
+ 0.1 (text-version)
    + +game.py
    + +marble.py
    + +showMarble.py
    + 텍스트 기반 홀짝게임 완성
+ 1.0 (GUI-version)
    + +game.py
    + +marble.py
    + +showMarble.py
    +GUI 기반 홀짝게임 완성
+ 1.1
    + /game.py
    + /marble.py
    + +opponent.py
    + +player.py
    + /showMarble.py
    + 지저분한 코드 정리. 개발의 편의를 위해 주석을 통한 설명 다수 추가. marble.py의 가독성 문제로 player.py와 opponent.py로 분리.

+ 1.2
    + + Image
    +noMarble.jpg
    +oneMarble.jpg
    +twoMarble.jpg
    +threeMarble.jpg
    +fourMarble.jpg
    +fiveMarble.jpg
    +sixMarble.jpg
    +win.jpg
    +lose.jpg
    + /game.py
    + /marble.py
    + /opponent.py
    + /showMarble.py
    + 이미지 파일들 추가 및 이미지 파일들을 출력하도록 수정함, 몇몇 필요 없는 변수 제거

+ 1.3
    + + Sound
    +backgroundmusic.mp3
    +getMarble.mp3
    +loseMarble.mp3
    +win.mp3
    +lose.mp3
    + /game.py
    + 소리 파일들 추가, 게임에서 소리가 나도록 수정

+ 1.4
    + /game.py
    + 배경음악 재생 위치 변경. (__main__에서 OddGame의 __init__으로)
