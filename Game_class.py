from random import randint


class Member(object):
    def setName(self, name):
        self.name = name

    def setCash(self, cash):
        self.cash = cash

    def __str__(self):
        return "Name: %s, Cash: %s" % (str(self.name), str(self.cash))


class TwiceDice(object):
    def eachDice(self):
        self.firstDice = randint(1, 6)
        self.secondDice = randint(1, 6)

    def __str__(self):
        return "Firstdice: %s, Seconddice: %s" % \
               (str(self.firstDice), str(self.secondDice))

    def diceSum(self):
        return self.firstDice + self.secondDice


class Game(object):
    def cashCheck(self, player01, player02):
        self.debt = 100
        print("player01 name: ", player01.name)
        print("player01 cash: ", player01.cash)
        print("player02 name: ", player02.name)
        print("player02 cash: ", player02.cash)

        if player01.cash < self.debt or player02.cash < self.debt:
            print("賭注金額不足，請重新輸入！")
        else:
            print("賭注金額已確認 \n遊戲開始！\n第 1 局")

    def randonGame(self, x, y, dice):
        if dice.diceSum() == 10 or dice.diceSum() == 11 or dice.diceSum() == 12:
            x.cash += self.debt
            y.cash -= self.debt
            print("玩家: %s win, 持有金額: %s" % (str(x.name), str(x.cash)))
            print("玩家: %s lose, 持有金額: %s" % (str(y.name), str(y.cash)))
        else:
            x.cash -= self.debt
            y.cash += self.debt
            print("玩家: %s win, 持有金額: %s" % (str(y.name), (y.cash)))
            print("玩家: %s lose, 持有金額: %s" % (str(x.name), (x.cash)))

    def firstPart(self, player01, player02, dice):
        if dice.diceSum() == 7 or dice.diceSum() == 11:
            player01.cash += self.debt
            player02.cash -= self.debt
            print("玩家: %s 勝" % player01.name)
        elif dice.diceSum() == 2 or dice.diceSum() == 3 or dice.diceSum() == 12:
            player01.cash -= self.debt
            player02.cash += self.debt
            print("玩家: %s 勝" % player02.name)
        else:
            print("無玩家勝出，進入第 2 局！")

    def secondPart(self, player01, player02, firstPartDice, dice):
        if dice.diceSum() == firstPartDice.diceSum():
            player01.cash += self.debt
            player02.cash -= self.debt
            print("玩家: %s 勝" % player01.name)
        elif dice.diceSum() == 7:
            player01.cash -= self.debt
            player02.cash += self.debt
            print("玩家: %s 勝" % player02.name)
        else:
            print("無玩家勝出，進入第 %s 局!" % num)



if __name__ == "__main__":
    playerA = Member()
    playerA.setName('Norman')
    playerA.setCash(1000)

    playerB = Member()
    playerB.setName('Kay')
    playerB.setCash(1200)

    firstGame = Game()
    firstGame.cashCheck(playerA, playerB)

    FirstRollDice = TwiceDice()
    FirstRollDice.eachDice()
    print(FirstRollDice.__str__())
    FirstRollDice.diceSum()


    firstGame.firstPart(playerA, playerB, FirstRollDice)
    if any(FirstRollDice.diceSum() == diceSum \
                for diceSum in (7, 11, 2, 3, 12)):
        pass
    else:
        num = 2
        go = True
        while go == True:
            num += 1
            newRollDice = "SecondRollDice" + str(num)
            newRollDice = TwiceDice()
            newRollDice.eachDice()
            print(newRollDice.__str__())
            newRollDice.diceSum()
            firstGame.secondPart(playerA, playerB, FirstRollDice, newRollDice)
            if any(newRollDice.diceSum() == diceSum \
                   for diceSum in (FirstRollDice.diceSum(), 7)):
                # go = False
                break
            else:
                go = True