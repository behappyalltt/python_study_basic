# 가현 1.
# date를 import해 Class dDay 생성 후 dday및 해당 날짜 출력하는 함수 생성해라
# ex) dday('2022-04-14") param 1개만 입력 시 현재 날짜와 비교
"""
import datetime

class dDay:
    def __init__(self, endDate, startDate = None):
        self.endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')

        if startDate == None:
            today = datetime.datetime.now()
            self.startDate = datetime.datetime(today.year, today.month, today.day)
        else:
            self.startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')

    def getDday(self):
        return (self.startDate - self.endDate).days

dDay = dDay("2022-04-14")
print(dDay.getDday())
"""

# 가현 2.
# math 를 import 해 class Circle생성 후 반지름 입력 받아 원의 둘레  원의 넓이 구하는 함수 생성
# 만약 입력 받은 반지름이 숫자가 아닐 경우 예외 처리
"""
import math

class Circle:
    def __init__(self, radius):
        if type(radius) == int or type(radius) == float:
            self.radius = radius
        else:
            return Exception

    def getRound(self):
        return self.radius * 2 * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi


circle = Circle(3)
print(circle.getRound())
print(circle.getArea())
"""

# 가현 3. 문자열 findall 함수가 빠른지 반복문이 빠른 지 성능 확인해보기