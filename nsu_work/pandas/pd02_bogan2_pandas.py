import numpy as np
import pandas as pd

data = pd.DataFrame([
    [2, np.nan, 6, 8, 10],
    [2, 4, np.nan, 8, np.nan],
    [2, 4, 6, 8, 10],
    [np.nan, 4, np.nan, 8, np.nan],
])
print(data)
#      0    1    2  3     4
# 0  2.0  NaN  6.0  8  10.0
# 1  2.0  4.0  NaN  8   NaN
# 2  2.0  4.0  6.0  8  10.0
# 3  NaN  4.0  NaN  8   NaN

data = data.transpose()   # 데이터 바꾸기(정리)
data.columns = ['x1', 'x2', 'x3', 'x4']
print(data)
#     x1   x2    x3   x4
# 0   2.0  2.0   2.0  NaN
# 1   NaN  4.0   4.0  4.0
# 2   6.0  NaN   6.0  NaN
# 3   8.0  8.0   8.0  8.0
# 4  10.0  NaN  10.0  NaN

print (data, data.shape) # (5, 4)

#0. 결측치 확인
print(data.isnull())
#       x1     x2     x3     x4
# 0  False  False  False   True
# 1   True  False  False  False
# 2  False   True  False   True
# 3  False  False  False  False
# 4  False   True  False   True

print (data.isnull().sum())
# x1    1
# x2    2
# x3    0
# x4    3
# dtype: int64

print(data.info())
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   x1      4 non-null      float64
#  1   x2      3 non-null      float64
#  2   x3      5 non-null      float64
#  3   x4      2 non-null      float64
# dtypes: float64(4)
# memory usage: 292.0 bytes

#1. 결측지 삭제
print(data.dropna)
# <bound method DataFrame.dropna of      x1   x2    x3   x4
# 0   2.0  2.0   2.0  NaN
# 1   NaN  4.0   4.0  4.0
# 2   6.0  NaN   6.0  NaN
# 3   8.0  8.0   8.0  8.0
# 4  10.0  NaN  10.0  NaN>

print(data.dropna(axis=0))
# <bound method DataFrame.dropna of      x1   x2    x3   x4
# 0   2.0  2.0   2.0  NaN
# 1   NaN  4.0   4.0  4.0
# 2   6.0  NaN   6.0  NaN
# 3   8.0  8.0   8.0  8.0
# 4  10.0  NaN  10.0  NaN>
#     x1   x2   x3   x4
# 3  8.0  8.0  8.0  8.0


print(data.dropna(axis=1))
#      x3
# 0   2.0
# 1   4.0
# 2   6.0
# 3   8.0
# 4  10.0

#2. 특정값 - 평균
means = data.mean()  # 판다스에서는 알아서 자동으로 컬럼별로 평균해줌
print(means)




data2 = data.fillna(means)
print(data2)
#      x3
# 0   2.0
# 1   4.0
# 2   6.0
# 3   8.0
# 4  10.0
# x1    6.500000
# x2    4.666667
# x3    6.000000
# x4    6.000000


# 2-2. 특정값 - 중위값
med = data.median()
print(med)
#      x1        x2    x3   x4
# 0   2.0  2.000000   2.0  6.0
# 1   6.5  4.000000   4.0  4.0
# 2   6.0  4.666667   6.0  6.0
# 3   8.0  8.000000   8.0  8.0
# 4  10.0  4.666667  10.0  6.0
# x1    7.0
# x2    4.0
# x3    6.0
# x4    6.0
# dtype: float64

data3 = data.fillna(med)
print(data3)
#      x1   x2    x3   x4
# 0   2.0  2.0   2.0  6.0
# 1   7.0  4.0   4.0  4.0
# 2   6.0  4.0   6.0  6.0
# 3   8.0  8.0   8.0  8.0
# 4  10.0  4.0  10.0  6.0


#2-3. 특정값 - 0
data4 = data.fillna(0)
print(data4)
#      x1   x2    x3   x4
# 0   2.0  2.0   2.0  0.0
# 1   0.0  4.0   4.0  4.0
# 2   6.0  0.0   6.0  0.0
# 3   8.0  8.0   8.0  8.0
# 4  10.0  0.0  10.0  0.0

#2-4. 특정값 - 777
data5 = data.fillna(777)
print(data5)
#       x1     x2    x3     x4
# 0    2.0    2.0   2.0  777.0
# 1  777.0    4.0   4.0    4.0
# 2    6.0  777.0   6.0  777.0
# 3    8.0    8.0   8.0    8.0
# 4   10.0  777.0  10.0  777.0

#2-5. 특정값 - ffill    # 시계열 잘먹힘, 첫번째가 없으면 nan
data6 = data.ffill()  
print(data6)
#      x1   x2    x3   x4
# 0   2.0  2.0   2.0  NaN
# 1   2.0  4.0   4.0  4.0
# 2   6.0  4.0   6.0  4.0
# 3   8.0  8.0   8.0  8.0
# 4  10.0  8.0  10.0  8.0

#2-5. 특정값 - bfill    # 시계열 잘먹힘, 마지막이 없으면 nan
data7 = data.bfill()
print(data7)
#      x1   x2    x3   x4
# 0   2.0  2.0   2.0  4.0
# 1   6.0  4.0   4.0  4.0
# 2   6.0  8.0   6.0  8.0
# 3   8.0  8.0   8.0  8.0
# 4  10.0  NaN  10.0  NaN

##################################################
med = data['x1'].median()
print(med)   # 6.5

mean = data['x4'].mean()
print(mean)     # 6.0

# 실습
"""
x1 : median
x2 : ffill
x4 : means    
    
"""
print("================================")

data['x1'] = data['x1'].fillna(med)
data['x2'] = data['x2'].ffill()
data['x4'] = data['x4'].fillna(mean)
print(data)
#      x1   x2    x3   x4
# 0   2.0  2.0   2.0  6.0
# 1   7.0  4.0   4.0  4.0
# 2   6.0  4.0   6.0  6.0
# 3   8.0  8.0   8.0  8.0
# 4  10.0  8.0  10.0  6.0