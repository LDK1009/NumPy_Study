import numpy as np

# 1차원 배열 간 사칙연산
a = np.arange(1, 6, 1)
b = np.arange(1, 6, 1)

print(a+b)  # >> [ 2  4  6  8 10]
print(a-b)  # >> [0 0 0 0 0]
print(a*b)  # >> [ 1  4  9 16 25]
print(a/b)  # >> [1. 1. 1. 1. 1.]


# 2차원 배열 간 사칙연산
a = np.arange(1, 10, 1).reshape(3, 3)
b = np.arange(1, 10, 1).reshape(3, 3)

print(a+b)  
print(a-b)  
print(a*b)  
print(a/b) 


# 배열 모든 요소에 연산 적용
a = np.arange(1, 10, 1)  # 1~9 배열 생성
b = a * 2
print(b)


