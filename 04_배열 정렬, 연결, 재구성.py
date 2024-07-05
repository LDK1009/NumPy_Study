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
y = np.array([[5, 6], [7,8]])
xy = np.concatenate((x, y), axis=1)
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

