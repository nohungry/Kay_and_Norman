from random import randint


class Member(object):
    def setName(self, name):
        self.name = name

    def setCash(self, cash):
        self.cash = cash

    def __str__(self):
        return "Name: %s, Cash: %s" % (str(self.name), str(self.cash))


class TwiceDice(object):
    def diceSum(self):
        self.firstDice = randint(1, 6)
        self.secondDice = randint(1, 6)
        return self.firstDice + self.secondDice

    def __str__(self):
        return "Firstdice: %s, Seconddice: %s" % \
               (str(self.firstDice), str(self.secondDice))


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
            print("賭注金額以確認")

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
    FirstRollDice.diceSum()
    print(FirstRollDice.__str__())
    firstGame.randonGame(playerA, playerB, FirstRollDice)