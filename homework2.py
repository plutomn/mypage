import random

print('가위 바위 보 게임')
print('가위 바위 보를 하는 게임 입니다.')

computer = random.choice(['가위', '바위', '보'])
player = input('가위 바위 보 중 하나를 입력하세요: ')

game_cnt = 1
com_win=0 # 컴퓨터가 이긴 횟수
me_win=0 # 내가 이긴 횟수

if computer == '가위':
    print('컴퓨터는 가위를 냈습니다.')
    if player == '가위':
        print('플레이어는 가위를 냈습니다.')
        print('무승부')
    elif player == '바위':
        print('플레이어는 바위를 냈습니다.')
        print('플레이어 승리')
        me_win += 1   
    elif player == '보':
        print('플레이어는 보를 냈습니다.')
        print('컴퓨터 승리')
        com_win += 1
elif computer == '바위':
    print('컴퓨터는 바위를 냈습니다.')
    if player == '가위':
        print('플레이어는 가위를 냈습니다.')
        print('컴퓨터 승리')
        com_win += 1
    elif player == '바위':
        print('플레이어는 바위를 냈습니다.')
        print('무승부')
    elif player == '보':
        print('플레이어는 보를 냈습니다.')
        print('플레이어 승리')
        me_win += 1
elif computer == '보':
    print('컴퓨터는 보를 냈습니다.')
    if player == '가위':
        print('플레이어는 가위를 냈습니다.')
        print('플레이어 승리')
        me_win += 1
    elif player == '바위':
        print('플레이어는 바위를 냈습니다.')
        print('컴퓨터 승리') 
        com_win += 1
    elif player == '보':
        print('플레이어는 보를 냈습니다.')
        print('무승부')
    
if com_win == me_win:
    print('비겼습니다.')
elif com_win > me_win:
    print('컴퓨터가 이겼습니다.')
else:
    print('내가 이겼습니다.')



if game_cnt > 5:
        game_continue = input('게임을 더 하시겠습니까?..("y/n")>>')
        if game_continue in ('n', 'N'):
            print('/게임을 종료합니다.')
        elif game_continue in ('y', 'Y'):
            game_cnt = 0
            me_win = 0
            com_win = 0
