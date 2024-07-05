import numpy as np
# 빈 배열 생성(난수 배열 생성)(메모리 상태에 따라 달라진다. 다른 코드 이후에 있으면 값이 달라지는 것을 확인할 수 있다.)
a = np.empty(2)
print(a) # >> [2.90351886e+083 1.53312588e+253]

# 랜덤 정수 배열 생성
rng = np.random.default_rng()  # 난수 생성 객체 생성
random_integers = rng.integers(5, size=(2, 4))# 0~4 랜덤 정수 값을 가지는 크기가 2행 4열인 배열 생성
print(random_integers)


# 0으로 채워진 1차원 배열 생성
a = np.zeros(2)
print(a) # >> [0. 0.]


# 1로 채워진 1차원 배열 생성
a = np.ones(2)
print(a) # >> [1. 1.]


# 균일하게 증가하는 배열 생성
a = np.arange(5) # 0~4까지 간격 1인 배열 생성
print(a) # >> [0 1 2 3 4]


# 범위 내 균일한 간격이 있는 배열 생성
a = np.arange(2, 10, 2) # 2~9까지 간격 2인 배열 생성
print(a) # >> [2 4 6 8]

# 선형적인 값이 있는 배열 생성
a = np.linspace(0, 10, num=5) # 0~10을 5구간으로 나누고 선형적으로 배치
print(a)