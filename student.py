class Student(object):

    # __init__是一個特殊方法用於在創建對象時進行初始化操作
    # 通過這個方法我們可以為學生對象綁定name和age兩個屬性
    # @property
    def __init__(self):
        print("初始化")
        # age = y
        # print("name:", name)
        # print("age", age)

    def study(self, course_name):
        # text = '%s正在學習%s.' % (self.name, course_name)
        # return text
        print('%s正在學習%s.' % (name, course_name))

    # PEP 8要求標識符的名字用全小寫多個單詞用下劃線連接
    # 但是部分程序員和公司更傾向於使用駝峰命名法(駝峰標識)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能觀看《熊出沒》.' % self.name)
        else:
            print('%s正在觀看島國愛情大電影.' % self.name)


if __name__ == "__main__":
    Student_A = Student()
    # Student_A.__init__()
    # Student_B = Student('B', 10)
    # print(Student_A.study)
    # print(Student_B.study
    # print(Student_A.age)

    # Student_A.study('BOOK_A')
    # Student_A.watch_movie()
    # Student_B.study('BOOK_B')
    # Student_B.watch_movie()
    # print(Student_B.name)
    # print(Student_B.age)
