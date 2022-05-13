# 가현 1. 두개의 정수를 입력받아 input함수와 print함수를 같이 사용하여 한 줄 프로그램을 완성
"""
a, b = map(int, input('정수 두 개를 입력하세요: ').split())
print(a, b)
"""

# 가현 2. 랜덤 함수를 이용해서 (1~10) 까지 맞출 때까지 while을 이용해 프로그램
"""
import random
randNum = random.randint(1, 10)
while True:
    guessNum = int(input("숫자를 입력하세요: "))
    if(guessNum == randNum):
        print("정답")
        break
"""

# 가현 3. 한개의 enum을 생성해 사용자가 입력받은 값을 통해 match case 문을 이용해 출력 (기타 제어 흐름 도구)
"""
from enum import Enum
class Rainbow(Enum):
    빨 = 'RED'
    주 = 'ORANGE'
    노 = 'YELLOW'
    초 = 'GREEN'
    파 = 'BLUE'
    보 = 'PURPLE'
    분 = 'PINK'

color = input("빨주노초파보분 중에 하나를 입력하세요: ")

match color:
    case '빨':
        print(Rainbow.빨.value)
    case '주':
        print(Rainbow.주.value)
    case '노':
        print(Rainbow.노.value)
    case '초':
        print(Rainbow.초.value)
    case '파':
        print(Rainbow.파.value)
    case '보':
        print(Rainbow.보.value)
    case '분':
        print(Rainbow.분.value)
"""

# 가현 4. 람다 표현식을 이용해 영문자 5개 내림차순 정렬
"""
alph = ['a', 'v', 'c', 's', 'k']
print(sorted(alph, key=lambda x : x[0], reverse = True))
"""

# 가현 5. 함수의 기본값(인자 기본값)이 계속되는 호출 시 누적되지 않도록 list에 append하는 함수 생성
"""
"""