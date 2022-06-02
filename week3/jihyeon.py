# 지현 1. 지나가 A~Z까지 쓰여져 있는 돌다리를 3개씩 건너려고 합니다. 지나가 밟은 알파벳들을 리스트와 슬라이싱을 이용하여 구하시오.
"""
from string import ascii_lowercase
alphabet_list = list(ascii_lowercase)
print(alphabet_list[::3])
"""

# 지현 3.
# 4 * 4 리스트에 0행 0열부터 2행 2열까지는 임의의 정수 값을 세팅하고 0행 3열, 1행 3열, 2행 3열에는 행값의 합을,
# 3행 0열, 3행 1열, 3행 2열에는 각 열의 핪을, 3행 3열에는 총합을 저장하시오.
"""
import random
nums = [[0] * 4 for i in range(4)]
for i in range(3):
    for j in range(3):
        num = random.randint(1, 10)
        nums[i][j] = num
        nums[i][3] += num
        nums[3][j] += num
        nums[3][3] += num
print(nums)
"""

