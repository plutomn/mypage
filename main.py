import random

random_number = random.randint(1, 100)
num = 0
t_cnt = 0 # 시도횟수

print("1~100 숫자 Up & Down 게임을 시작합니다 !!!")
print("---------------------------")

while True:
        try:
            #if 100 < num and 1 > num:   : 적용이안됨
                #print("범위가 넘어간 숫자입니다") : 보류상태

            num = int(input("1 ~ 100 사이의 숫자를 입력하세요 : "))

            if (num > random_number):
                print("Down")
                t_cnt += 1
            elif (num < random_number):
                print("Up")
                t_cnt += 1       
            elif (num == random_number):
                print(t_cnt, "번 만에 정답을 맞추셨습니다.")
                i = str(input('한 판 더? (Y/N) '))
                if i == 'y' or i == 'Y' :
                   i
                elif i == 'n' or i == 'N':
                    break
                else :
                     print("애러입니다")


        except ValueError:
            print("숫자만 입력하세요")

#불완전한것
 # 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요.
    # - 기능은 추가하였으나  Y 와 N 값이외에 문자를 입력제한하는것을 하지못함, 왜 돌아가는지 모름( 숫자 답또한 동일값으로 돌아감)

 # 플레이어가 입력한 숫자가 범위를 벗어날 경우, 적절한 안내 메시지를 출력하여 유효한 범위 내의 숫자를 입력하도록 유도하세요

 # 게임이 종료될 때 플레이어의 최고 시도 횟수를 기록하고, 다음 게임에서 이를 표시하는 기능을 구현하세요.
  # 강의내용 숙지 부족

       