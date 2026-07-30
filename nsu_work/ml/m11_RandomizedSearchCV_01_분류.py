# 09_1 카피

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.model_selection import StratifiedKFold,GridSearchCV,RandomizedSearchCV
from sklearn.datasets import load_iris 
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import r2_score
from xgboost import XGBClassifier
import time
    

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

KFold = StratifiedKFold(n_splits=5, shuffle=True, random_state=123)             # keyvalue = 무조건 dictionary
# Fitting 5 folds for each of 10 candidates, totalling 50 fits



#2. 모델
parameters = [
    {"C": [1,10,100,1000], "kernel":['linear', 'sigmoid'], "degree": [3,4,5]},   
    {"C": [1,10,100], "kernel":['rbf'], 'gamma':[0.001, 0.0001]},
    {"C": [1,10,100,1000], "kernel":['sigmoid'],
    "gamma": [0.01, 0.001, 0.0001], "degree":[3,4,5]},    # 36
    # 24 + 6 + 36 = 66
]



model = RandomizedSearchCV(XGBClassifier(),parameters, cv=KFold, verbose=1,) 
# Fitting 5 folds for each of 10 candidates, totalling 50 fits

# 컴파일 , 훈련
start_time = time.time()


model.fit(x_train,y_train)

 
print("최적의 매개변수 : ", model.best_estimator_)


print("최적의 파라미터 : ", model.best_params_)
# 최적의 파라미터 :  {'kernel': 'sigmoid', 'gamma': 0.01, 'degree': 4, 'C': 1000}

end_time = time.time() 
#4. 평가, 예측
print('best_score : ', model.best_score_)
# best_score :  0.9583333333333333

print('model.score : ', model.score(x_test, y_test))
# model.score :  0.9

y_predict = model.predict(x_test)
print("r2_score : ", r2_score(y_test, y_predict))
# r2_score :  0.85

print("걸린시간 : ", round(end_time - start_time, 2), '초')
# 걸린시간 :  1.19 초


# 분류 : Classfier, accuracy,  회귀 : Regressor, r2
# 분류 : learning_rate, max_depth   회귀 : Kernel, degree