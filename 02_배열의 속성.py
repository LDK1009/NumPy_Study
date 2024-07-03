import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


# 배열의 차원수
print(a.ndim) # >> 2


# 각 차원의 요소 개수(튜플로 반환)
print(a.shape) # >> (3, 4)


# 배열 내 요소의 총 개수
print(a.size)


# 배열 내 요소의 데이터 유형
print(a.dtype)