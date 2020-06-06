"""
craps賭博遊戲
Norman是玩家，Kay是莊家，玩 5 次(局)後，計算哪一方贏最多，那一方可以要求對方做一件事 <3
"""
from random import randint


money = int(input('請輸入你的資產: '))
sum = 0
player = 0
kay = 0
while money > 0 and sum < 5:
    needs_go_on = False
    while True:
        while sum > 0:
            print('您目前的資產: ', money)
            print('已玩 %d 局, Norman贏 %d 局, Kay贏 %d 局' % (sum, player, kay))
            break
        debt = int(input('請輸入投注金額: '))
        if debt < 0:
            print('您的投注額小於0，請重新輸入!')
        elif debt == 0:
            print('您的投注額等於0，請重新輸入!')
        elif debt > money:
            print('您的投注額大於您的資產，請重新輸入!')
        else:
            print('遊戲開始!')
            break
    first = randint(1, 6) + randint(1, 6)
    print('Python搖出: %d 點' % first)
    if first == 7 or first == 11:
        print('這一局Norman贏了!')
        # money = money + debt
        money += debt
        player += 1
        sum += 1
    elif first == 2 or first == 3 or first == 12:
        print('這一局Kay贏了!')
        money -= debt
        kay += 1
        sum += 1
    else:
        needs_go_on = True
        print("need go on method up")

    while needs_go_on == True:
        current = randint(1, 6) + randint(1, 6)
        run_num = 1
        print('Python搖出: %d 點' % current)
        if current == first:
            print('這一局您贏了!')
            money += debt
            player += 1
            sum += 1
            rum_num += 1
            print("二次random總共跑: ", run_num)
            needs_go_on = False
        elif current == 7:
            print('這一局Kay贏了!')
            money - + debt
            kay += 1
            sum += 1
            run_num += 1
            print("二次random總共跑: ", run_num)
            needs_go_on = False
        else:
            run_num += 1
            needs_go_on = True

print('遊戲結束!\n總結: Norman贏 %d 局, Kay贏 %d 局' % (player, kay))
if player > kay:
    print('我們的遊戲結束囉~，運氣真好ㄎㄎ')
else:
    print('哈哈哈 Kay贏了 你要乖乖聽Kay的話!')
