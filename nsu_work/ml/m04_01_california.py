# 회귀

import numpy as np
from sklearn.datasets import fetch_california_housing

x, y = fetch_california_housing(return_X_y=True)
print(x.shape, y.shape)   # (20640, 8) (20640,)

#2. 모델구성
from sklearn.svm import LinearSVC              # Linear, Regress = 회귀
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# model = LinearSVC()   # 분류라 안됨
# model = LogisticRegression()   # 분류라 안됨 ,   Regress 중 LogisticRegression =  유일하게 분류
# model = DecisionTreeRegressor()   # 1.0                        # 회귀
model = RandomForestRegressor()     # 0.9741241388511516
# Randomforest가 성능이 가장 좋음
# 그전에는 3가지 더 좋은게 있음, 실무에서 주로 사용


#3. 컴파일, 훈련
model.fit(x, y)

#4. 평가, 예측
results = model.score(x, y)
print(results)