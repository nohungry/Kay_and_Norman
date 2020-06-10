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

class Activity():
    def who(self, name, sex="Female"):
        self.name = name
        self.sex = sex
        return self.name, sex

    def where(self, location, district, weather):
        self.location = location
        return "It is %s in %s." % (weather, district)

    def when(self, time=14):
        self.time = time

    def what(self):
        if self.sex == "Female":
            if self.time >= 9 and self.time < 13:
                return "%s is having brunch at %s." % (self.name, self.location)
            elif self.time >= 13 and self.time < 17:
                return "%s is having afternoon tea at %s." % (self.name, self.location)
            else:
                return "%s is sleeping at %s." % (self.name, self.location)
        elif self.sex == "Male":
            return "%s is at %s at %s." % (self.name, self.location, str(self.time))



if __name__ == "__main__":
    # norman = Norman()
    # print(norman.toDo("10: 00", action=1))
    # print(norman.toDo("11: 00", action=1))
    # print(norman.test())

    kay = Activity()
    kay.who("Kay")
    kay.where("agnès b.", "Xinyi District", "sunny")
    kay.when()
    print(kay.what())

    norman = Activity()
    norman.who("Norman", "Male")
    norman.where("天堂 office", "Xinyi District", "sunny")
    norman.when("noon")
    print(norman.what())




