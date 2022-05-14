# 지현 1. 이름과 나이 변수를 가지고 있으며, 나이를 통해 태어난 년도를 구하는 함수를 가지고 있는 클래스를 작성하세요.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getBirthYear(self):
        return 2022 - self.age + 1

me = Person("지현", 24)
print(me.getBirthYear())
"""

# 지현 2. random 함수를 이용하여 로또 번호를 추출하고, 출력하세요. (1~45까지, 6개)
"""
import random

lotto = []

for i in range(6):
	lotto.append(random.randint(1, 45))
	
print(lotto)
"""

# 지현 3. sleep 함수를 이용하여 1초에 한 번씩 지금 시간을 출력하고, 30초 후에 종료되는 프로그램을 작성하세요.
"""
import time
import datetime

end_time = time.time() + 30
while True:
	if time.time() > end_time:
		break;
	print(datetime.datetime.now())
	time.sleep(1)
"""