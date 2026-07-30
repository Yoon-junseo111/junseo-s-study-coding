# 08_1 카피

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.datasets import fetch_california_housing, load_iris
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestRegressor
import numpy as np
#1. 데이터
x, y = fetch_california_housing(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, shuffle=True, random_state=333, train_size=0.8,
                                                       #  stratify = 균형있게 자르기
)
# print(y_train)
# print(y_test)
# print(np.unique(y_train))
# exit()

# KFold = KFold(n_splits=5, shuffle=True, random_state=123)
KFold = StratifiedKFold(n_splits=5, shuffle=True, random_state=123)   # ACC :  [0.96666667 0.96666667 0.93333333 1.         0.9       ] 



#2. 모델
# model = DecisionTreeRegressor()
# 07_1 카피

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold
import numpy as np
#1. 데이터
x, y = load_iris(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, shuffle=True, random_state=333, train_size=0.8,
    stratify=y                                                   #  stratify = 균형있게 자르기
)
# print(y_train)
# print(y_test)
# print(np.unique(y_train))
# exit()

# KFold = KFold(n_splits=5, shuffle=True, random_state=123)
KFold = StratifiedKFold(n_splits=5, shuffle=True, random_state=123)   # ACC :  [0.96666667 0.96666667 0.93333333 1.         0.9       ] 



#2. 모델
# model = DecisionTreeClassifier()   # cross_val_score 평균:  0.9533
model = RandomForestRegressor()   # cross_val_score 평균:  0.9517

#3. 컴파일, 훈련
#4. 평가, 예측
scores = cross_val_score(model, x, y, cv=KFold, n_jobs=-1)   # njobs = cpu 몇개 쓸껀지  -1은 cpu 전체

print('ACC : ', scores,
      '\n cross_val_score 평균: ',round(np.mean(scores),4)   # round = 값 반올림
      )  #  cross_val_score 평균:  0.96





#3. 컴파일, 훈련
#4. 평가, 예측
scores = cross_val_score(model, x, y, cv=KFold, n_jobs=-1)   # njobs = cpu 몇개 쓸껀지  -1은 cpu 전체

print('ACC : ', scores,
      '\n cross_val_score 평균: ',round(np.mean(scores),4)   # round = 값 반올림
      )  #  cross_val_score 평균:  0.96

