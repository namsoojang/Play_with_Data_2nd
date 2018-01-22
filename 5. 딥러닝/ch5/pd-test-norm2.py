import pandas as pd
# 키, 체중, 유형 데이터프레임 생성하기
tbl = pd.DataFrame({
    "weight": [ 80.0, 70.4, 65.5, 45.9, 51.2, 72.5 ],
    "height": [ 170,  180,  155,  143,  154,  160  ],
    "gender": [ "f",  "m",  "m",  "f",  "f",  "m"  ]
})
# 키와 몸무게 정규화하기
# 최댓값과 최솟값 구하기
def norm(tbl, key):
    c = tbl[key]
    v_max = c.max()
    v_min = c.min()
    print(key, "=", v_min, "-", v_max)
    tbl[key] = (c - v_min) / (v_max - v_min)
norm(tbl, "weight")
norm(tbl, "height")
print(tbl)