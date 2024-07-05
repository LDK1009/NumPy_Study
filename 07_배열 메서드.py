import numpy as np

# 1차원 배열 요소들의 집계 함수
a = np.arange(1, 6, 1)
print(a.max()) # axis로 축 지정이 가능하다
print(a.min())
print(a.sum())
print(a.sum())
print(a.sum())


# 2차원 배열 요소들의 집계 함수
a = np.arange(1, 10, 1)  # 1~9 배열 생성
a = a.reshape(3, -1)  # 3행 3열로 변경
print()
print()
print()
print(a.sum(axis=0))  # 열에 대한 합 [12 15 18]
print(a.sum(axis=1))  # 행에 대한 합 [ 6 15 24]
print(a.max(axis=0))  # 열에 대한 최대값 [7 8 9]
print(a.max(axis=1))  # 행에 대한 최대값 [3 6 9]


# 배열 내 중복값 제거(2차원 배열에도 적용 가능하며 axis를 통해 축을 결정할 수 있다)
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 11, 12, 13, 14,])
unique_values = np.unique(a) # >> 고유값만을 리턴한다. 즉, 중복값을 제거한다.
# unique_values = np.unique(a, axis=0) # >> 2차원 배열의 경우 axis를 통해 축을 결정할 수 있다.
print(unique_values) # >> [11 12 13 14 15 16 17 18 19 20]

# 배열 내 고유값 인덱스 찾기
unique_values, indices_list = np.unique(a, return_index='True') 
print(unique_values) # >> 고유값 배열 리턴한다.
print(indices_list)  # >> 고유값들의 인덱스를 리턴한다.

# 배열 내 고유값 개수 찾기
unique_values, occurrence_count = np.unique(a, return_counts=True)
print(unique_values) # >> 고유값 배열 리턴한다.
print(occurrence_count) # >> 고유값의 개수 리턴한다.

# 배열 내 고유값, 인덱스, 고유값 개수 찾기
unique_rows, indices_list, occurrence_count = np.unique(a, return_counts=True, return_index=True)
print(unique_rows)
print(indices_list)
print(occurrence_count)
