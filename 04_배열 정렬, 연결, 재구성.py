import numpy as np

# 배열 정렬
a = np.array([2, 1, 5, 3, 7, 4, 6, 8])
sort_a = np.sort(a) # 기존 배열 정렬이 아니다. 기존 배열을 정렬한 사본을 반환한다.
print(sort_a)


# 1차원 배열 2개 연결하기
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.concatenate((a, b))
print(c)

# 2차원 배열 2개 연결하기
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
xy = np.concatenate((x, y), axis=0)
print(xy)


# 배열 재구성하기
a = np.arange(6) # 1차원 배열 생성
b = a.reshape(3, 2) # 3행 2열로 재구성
print(b)

# 배열 축(axis) 추가하기
a = np.arange(5)
a1 = a[np.newaxis, :] # 행 벡터로 추가
a2 = a[:, np.newaxis] # 열 벡터로 추가
print(a1.shape)
print(a1)
print(a2.shape)
print(a2)

# 축을 추가하는 다른 방법
# b = np.expand_dims(a, axis=1)
# c = np.expand_dims(a, axis=0)


# 1차원 배열에서 조건을 충족하는 값만 추출
a = np.arange(5) # [0, 1, 2, 3, 4]
b = a[a>2] # 3이상만 추출
print(b)

# 2차원 배열에서 조건을 충족하는 값만 추출
a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = a[a>2]
print(b) # 1차원 배열로 변환되는 것을 확인할 수 있다.

# 조건문 활용(조건을 변수에 담아 대입하기)
a = np.arange(10) # [0, 1, 2, 3, 4]
two_five = (a >= 2) & (a<=5)
print(a[two_five])