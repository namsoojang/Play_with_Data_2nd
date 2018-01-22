import pandas as pd
# 키, 몸무게, 유형 데이터프레임 생성하기
tbl = pd.DataFrame({
    "weight": [ 80.0, 70.4, 65.5, 45.9, 51.2 ],
    "height": [ 170,  180,  155,  143,  154  ],
    "type":   [ "f", "n", "n", "t", "t"]
})
# 몸무게 목록 추출하기
print("몸무게 목록")
print(tbl["weight"])
# 몸무게와 키 목록 추출하기
print("몸무게와 키 목록")
print(tbl[["weight","height"]])