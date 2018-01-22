import numpy as np
# 10개의 float32 자료형 데이터 생성
v = np.zeros(10, dtype=np.float32)
print(v)
# 연속된 10개의 uint64 자료형 데이터 생성
v = np.arange(10, dtype=np.uint64)
print(v)
# v 값을 3배하기
v *= 3
print(v)
# v의 평균 구하기
print(v.mean())