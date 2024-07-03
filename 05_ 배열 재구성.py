import numpy as np


# 배열 재구성하기
a = np.arange(6)  # 1차원 배열 생성
b = a.reshape(3, 2)  # 3행 2열로 재구성
print(b)


# 배열 축(axis) 추가하기
a = np.arange(5)
a1 = a[np.newaxis, :]  # 행 벡터로 추가
a2 = a[:, np.newaxis]  # 열 벡터로 추가
print(a1.shape)
print(a1)
print(a2.shape)
print(a2)


# 두개의 2차원 배열 합치기
a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])

# 두개의 2차원 배열 수직으로 쌓기
a3 = np.vstack((a1, a2))  # 괄호가 2개임을 유의해야한다.
print(a3)

# 두개의 2차원 배열 수평으로 쌓기
a3 = np.hstack((a1, a2))
print(a3)


# 배열 분할하기(분할한 배열은 얕은 복사된다.)
a = np.arange(1, 25).reshape(2, 12) # 2행 12열 2차원 배열 생성
a_split = np.hsplit(a, 3) # 배열을 3개로 균등하게 분할
print(a_split)

# 구한 정해서 배열 분할하기
a = np.arange(1, 25).reshape(2, 12) # 2행 12열 2차원 배열 생성
a_split = np.hsplit(a, (3,4)) # 배열을 3개로 균등하게 분할하되 3열에서 4열은 제외
print(a_split)
