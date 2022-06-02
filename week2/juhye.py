# 주혜 1. 학생 5명의 수학 시험 점수를 랜덤으로 지정한 뒤, 학생들의 점수 평균값을 구하시오
"""
import random

sum = 0
grades = []

for i in range(5):
    grade = random.randint(1, 100)
    grades.append(grade)
    sum += grade

print(grades)
print(sum / 5)

statistics.mean()
"""

# 주혜 2.class를 생성한 뒤, 그 안에 2개의 숫자의 최소공배수를 구하는 메서드를 만들고, 객체를 생성하여 메서드 결과값을 출력하시오
"""
import math

class Exam:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def getLeastCommonMultiple(self):
        return math.lcm(self.num1, self.num2)

numbers = Exam(15, 25)
print(numbers.getLeastCommonMultiple())
"""

# 주혜 3. 자신이 원하는 URL을 접속하여 결과값을 출력하시오.
"""
import requests

url = "https://github.com/ganellope/python-study"
req = requests.get(url)
print(req.text)
"""