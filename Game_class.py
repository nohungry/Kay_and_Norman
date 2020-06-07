from random import randint


class Member(object):
    def setName(self, name):
        self.name = name

    def setCash(self, cash):
        self.cash = cash

    def __str__(self):
        return "Name: %s, Cash: %s" % (str(self.name), str(self.cash))


class TwiceDice(object):
    # 為什麼這裡需要外部參數帶入呢???  27行 帶入外部參數 firstDice, secondDice
    def eachDice(self, firstDice, secondDice):
        firstDice = randint(1, 6)
        secondDice = randint(1, 6)
        self.firstDice = firstDice
        self.secondDice = secondDice

        return self.firstDice + self.secondDice

    def __str__(self):
        return "Firstdice: %s, Seconddice: %s" % \
               (str(self.firstDice), str(self.secondDice))

    def diceSum(self, one, two):
        return one + two



class Game(object):
    def cashCheck(self, player01, player02):
        self.debt = 100
        print("player01 name: ", player01.name)
        print("player01 cash: ", player01.cash)
        print("player02 name: ", player02.name)
        print("player02 cash: ", player02.cash)

        if player01.cash < self.debt or player02.cash < self.debt:
            print("賭注金額不足")
        else:
            print("賭注金額已確認")

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
        if dice.diceSum == 7 or dice.diceSum == 11:
            player01.cash += self.debt
            player02.cash -= self.debt
            print("玩家: %s 勝" % player01.name)
        elif dice.diceSum == 2 or dice.diceSum == 3 or dice.diceSum == 12:
            player01.cash -= self.debt
            player02.cash += self.debt
            print("玩家: %s 勝" % player02.name)
        else:
            print("無玩家勝出，進入第二局！")

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
            print("進入第%f局" % partNumber)



if __name__ == "__main__":
    playerA = Member()
    playerAName = 'Norman'
    playerACash = 1000
    playerA.setName(playerAName)
    playerA.setCash(playerACash)

    playerB = Member()
    playerBName = 'Kay'
    playerBCash = 1200
    playerB.setName(playerBName)
    playerB.setCash(playerBCash)

    firstGame = Game()
    firstGame.cashCheck(playerA, playerB)

    FirstRollDice = TwiceDice()
    FirstRollDice.eachDice()
    print(FirstRollDice.__str__())
    FirstRollDice.diceSum(FirstRollDice.eachDice.firstDice, FirstRollDice.eachDice.secondDice)

    firstGame.firstPart(playerA, playerB, FirstRollDice)
    if FirstRollDice.diceSum != 7 and FirstRollDice.diceSum != 11 and \
        FirstRollDice.diceSum != 2 and FirstRollDice.diceSum != 3 and \
        FirstRollDice.diceSum != 12:
        print("Go")
    else:
        print("x")