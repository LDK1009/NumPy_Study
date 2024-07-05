import numpy as np


# 배열 재구성하기
a = np.arange(6)  # 1차원 배열 생성
b = a.reshape(3, 2)  # 3행 2열로 재구성
print("==========배열 재구성하기")
print(b)


# 배열 축(axis) 추가하기
a = np.arange(5)
a1 = a[np.newaxis, :]  # 행 벡터로 추가
a2 = a[:, np.newaxis]  # 열 벡터로 추가
print("==========배열 축(axis) 추가하기")
print(a1.shape)
print(a1)
print(a2.shape)
print(a2)


# 배열 축 반전
a = np.arange(1, 10, 1).reshape(3, 3)  # 1~9값을 가진 3행 3열 배열 생성
b = a.transpose()
# b = a.T # 동일한 기능 수행
print("==========배열 축 반전")
print(a)
print(b)


# 배열 뒤집기
a = np.arange(1, 10, 1).reshape(3, 3)  # 1~9값을 가진 3행 3열 배열 생성
reverse_a = np.flip(a)  # 모든 값의 순서를 뒤집는다
reversed_row_a = np.flip(a, axis=0)  # 모든 행의 순서를 뒤집는다
reversed_col_a = np.flip(a, axis=1)  # 모든 열의 순서를 뒤집는다
reversed_row0_a = np.flip(a[0])  # 0행의 값의 순서만 뒤집는다
print("==========배열 뒤집기")
print(reverse_a)
print(reversed_row_a)
print(reversed_col_a)
print(reversed_row0_a)


# 두개의 2차원 배열 합치기
a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])
print("==========두개의 2차원 배열 합치기")
# 두개의 2차원 배열 수직으로 쌓기
a3 = np.vstack((a1, a2))  # 괄호가 2개임을 유의해야한다.
print(a3)
# 두개의 2차원 배열 수평으로 쌓기
a3 = np.hstack((a1, a2))
print(a3)


# 배열 분할하기(분할한 배열은 얕은 복사된다.)
a = np.arange(1, 25).reshape(2, 12)  # 2행 12열 2차원 배열 생성
a_split = np.hsplit(a, 3)  # 배열을 3개로 균등하게 분할
print("==========배열 분할하기")
print(a_split)

# 구한 정해서 배열 분할하기
a = np.arange(1, 25).reshape(2, 12)  # 2행 12열 2차원 배열 생성
a_split = np.hsplit(a, (3, 4))  # 배열을 3개로 균등하게 분할하되 3열에서 4열은 제외
print("==========구간 정해서 배열 분할하기")
print(a_split)
