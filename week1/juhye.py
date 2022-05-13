# 주혜 1. 한 개의 정수를 입력받은 뒤, 약수 리스트를 구하고, 구해진 약수의 각 거듭제곱 값을 모두 합한 값을 리턴하는 프로그램
"""
def func1():
    num = int(input("정수를 입력하세요: "))
    sum = 0
    print("약수: ", end="")
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=" ")
            sum += (i*i)
    print("\n약수의 거듭제곱 합: ", end="")
    print(sum)
"""

# 주혜 2.
# 2개 이상의 단어로 이루어진 문자열을 입력받는다.(단어 간 스페이스바로 공백 넣기)
# - 각 단어의 알파벳의 위치가 홀수인 경우 => 대문자
# - 각 단어의 알파벳의 위치가 짝수인 경우 => 소문자
# 위 조건에 맞게 변경한 값을 리턴하는 프로그램
"""
def func2():
    words = [word for word in input().split()]
    for i in range(0, len(words)):
        if(i % 2 == 0):
            print(words[i].upper())
        else:
            print(words[i].lower())
"""

# 주혜 3. 연수 입력받아서 입력받은 수 만큼 별을 찍어봅시다! (가능하다면 리스트 컴프리헨션을 사용해봅시다)
"""
num = int(input("입력값: "))
for i in range(num+1):
    for j in range(num-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print("")
"""

# 주혜 4.
# classOne = {'정지나':'여', '이대형':'남', '정혜선':'여', '제이슨':'남', '손주혜':'여'}
# classTwo = {'이가현':'여', '함기훈':'남', '박향규':'남', '이지현':'여', '신혜정':'여', '권오재':'남'}
# 1반과 2반의 학생들을 합친 뒤, 성별로 구분지어서 출력한다.
"""
def func3():
    classOne = {'정지나':'여', '이대형':'남', '정혜선':'여', '제이슨':'남', '손주혜':'여'}
    classTwo = {'이가현':'여', '함기훈':'남', '박향규':'남', '이지현':'여', '신혜정':'여', '권오재':'남'}
    allClass = dict(classOne, **classTwo)
    print("~ 여자 ~")
    for key, value in allClass.items():
        if '여' == value:
            print(key)
    print("\n~ 남자 ~")
    for key, value in allClass.items():
        if '남' == value:
            print(key)
"""

# 주혜 5. 정수 10개를 입력받고, 10개의 숫자 중 가장 작은 값, 가장 큰 값, 중간 값을 출력한다.
"""
print("정수 10개를 입력하세요(공백으로 구분)")
nums = [int(i) for i in input().split()]
nums.sort()
print("가장 큰 값: " + str(max(nums)))
print("중간 값: " + str(nums[int(10/2)]))
print("가장 작은 값: " + str(min(nums)))
"""