# 09_1 카피

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold,GridSearchCV
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
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

KFold = KFold(n_splits=5, shuffle=True, random_state=123)             # keyvalue = 무조건 dictionary   그냥 kfold는 분류
# KFold = StratifiedKFold(n_splits=5, shuffle=True, random_state=123)  



#2. 모델
parameters = [
    {"C": [1,10,100,1000], "kernel":['linear', 'sigmoid'], "degree": [3,4,5]},   
    {"C": [1,10,100], "kernel":['rbf'], 'gamma':[0.001, 0.0001]},
    {"C": [1,10,100,1000], "kernel":['sigmoid'],
    "gamma": [0.01, 0.001, 0.0001], "degree":[3,4,5]},    # 36
    # 24 + 6 + 36 = 66
]
# keyvalue = 무조건 dictionary, "C" = dictionary


model = GridSearchCV(LinearSVC(),parameters, cv=KFold, verbose=1,) 
# model = SVC()
start_time = time.time()

#3. 컴파일, 훈련


model.fit(x_train,y_train)
# Fitting 5 folds for each of 66 candidates, totalling 330 fits
 
print("최적의 매개변수 : ", model.best_estimator_)
# 최적의 매개변수 :  SVC(C=1, kernel='linear')

print("최적의 파라미터 : ", model.best_params_)
# 최적의 파라미터 :  {'C': 1, 'degree': 3, 'kernel': 'linear'}

end_time = time.time()   # 걸린시간 :  0.46 초
#4. 평가, 예측
print('best_score : ', model.best_score_)
# best_score :  0.9916666666666668

print('model.score : ', model.score(x_test, y_test))
# model.score :  0.9666666666666667

y_predict = model.predict(x_test)
print("acc_score : ", accuracy_score(y_test, y_predict))
# acc_score :  0.9666666666666667                         # acc_score = predict


print("걸린시간 : ", round(end_time - start_time, 2), '초')



