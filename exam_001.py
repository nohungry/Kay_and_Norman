"""
此次題目為: 透過class來敘述KAY的一天(include 時間 事情 心情 外出)

            1. 需要使用外部參數 def xxx(x, y, z) (位置外部參數)
            2. 可以測試並使用固定的外部參數 def xxx(x=1, y=2, z=3) (關鍵字外部參數)
            3. def xxx((位置外部參數), (關鍵字外部參數))  **EX. def xxx(x, y, test=0)** 一定要先設置位置參數,在填寫關鍵字參數
"""


class Norman():
    """
    time 我自己設定的預設格式為: 00:00 ~ 24:00 (str)
    action 我自己設定的預設格式為: 0, 1, 2, 3, 4, 5
    """

    def toDo(self, time, action=0):
        self.time = time
        if action == 0:
            return "time: %s, Norman is doing nothing" % str(self.time)

        elif action == 1:
            return "time: %s, Norman is reading" % str(self.time)

    def outside(self):
        pass

    def mocation(self):
        pass

    def test(self):
        return self.time

class Kay():
    def atHome(self, clothing, mood, time, doing=0):
        self.clothing = clothing
        self.mood = mood
        if doing == 0:
            pass
        return "It's %s o'clock. Kay put on a %s, and looked %s." \
            % (str(time), self.clothing, self.mood)

    def outside(self, location, spendmoney=250):
        return "Kay is wearing %s now. She looks %s because she is waiting for Norman at %s.\
        Kay is hungry now so she spends $%s for her lunch." \
               % (self.clothing, self.mood, location, spendmoney)


if __name__ == "__main__":
    norman = Norman()
    print(norman.toDo("10: 00", action=1))
    print(norman.toDo("11: 00", action=1))
    print(norman.test())

    kay = Kay()
    print(kay.atHome("dress", "happy", 10, 1))
    print(kay.outside("Breeze Nan Shan"))



