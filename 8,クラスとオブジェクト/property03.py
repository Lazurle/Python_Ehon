# ◆ プロパティ(2)
class Student:
    def __init__(self, n):
        self.__name = n
        self.__score = [0]

    @property
    def name( self ): # nameは読み取り専用のプロパティ、ゲッター
        return self.__name

    @property # scoreのゲッター
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if 0 <= score <= 100:
            self.__score = score
            print(self.__name, "=", self.__score)
        else:
            print('0から100までの値を入力してください。')

students = [None]*3 # 空の３個分のリストを作る
students[0] = Student('Alan')
students[1] = Student('Becky')
students[2] = Student('Carl')
students[0].score = 78
students[1].score = 460
students[1].score = 46
students[2].score = 98

for st in stundents:
    print(st.name, "さんは", st.score, "点です。")
