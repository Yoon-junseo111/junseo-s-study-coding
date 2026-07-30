# 09_2 카피
# 그리드서치를 랜덤서치로 바꾸고 성능비교


from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.datasets import fetch_california_housing
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold,GridSearchCV,RandomizedSearchCV
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import r2_score
import time
from xgboost import XGBRegressor

    

#1. 데이터
x, y = fetch_california_housing(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, shuffle=True, random_state=333, train_size=0.8,
    # stratify=y                                                   #  stratify = 균형있게 자르기
)
# print(y_train)
# print(y_test)
# print(np.unique(y_train))
# exit()

KFold = KFold(n_splits=5, shuffle=True, random_state=123)             # keyvalue = 무조건 dictionary
# KFold = StratifiedKFold(n_splits=5, shuffle=True, random_state=123)  



#2. 모델
parameters = [
    {'n_estimators': [100,200], "max_depth":[6, 10, 12], #"degree": [3,4,5]},   
    'learning_rate' : [0.1, 0.01, 0.001]},  # 18
    {'max_depth':[6,8,10,12], 'learning_rate':[0.1,0.01,0.001]}, #12
    {'min_child_weight': [2,3,5,10], 'learning_rate':[0.1, 0.01, 0.001]}, #12
    # 18 + 12 + 12 = 40
]
# keyvalue = 무조건 dictionary, "C" = dictionary


model = RandomizedSearchCV(XGBRegressor(),parameters, cv=KFold, verbose=1,) 
# model = SVC()
start_time = time.time()

#3. 컴파일, 훈련


model.fit(x_train,y_train)
print("최적의 매개변수 : ", model.best_estimator_)
print("최적의 파라미터 : ", model.best_params_)
# 최적의 파라미터 :  {'n_estimators': 200, 'max_depth': 6, 'learning_rate': 0.1}

end_time = time.time()   


#4. 평가, 예측
print('best_score : ', model.best_score_)
# best_score :  0.8399064254001534

print('model.score : ', model.score(x_test, y_test))
# model.score :  0.8357082683009049

y_predict = model.predict(x_test)
print("r2_score : ", r2_score(y_test, y_predict))
# r2_score :  0.8357082683009049          


print("걸린시간 : ", round(end_time - start_time, 2), '초')
# 걸린시간 :  18.21 초



# xgboost, LGBM, Catboost : 부스트모델 성능 3순위