# 10_1 카피
# xgb로 만든다

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.model_selection import StratifiedKFold,GridSearchCV
from sklearn.datasets import fetch_california_housing
import numpy as np
from sklearn.metrics import r2_score
import time
from xgboost import XGBRegressor

    

#1. 데이터
x, y = fetch_california_housing(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, shuffle=True, random_state=333, train_size=0.8,
    # stratify=y                                                   
)


#2. 모델
parameters = {    
    "learning_rate" : 0.1,
    "max_depth": 6,
    "n_estimators" : 200,
}
  
   
  

model = XGBRegressor(**parameters)


#3. 컴파일, 훈련
start_time = time.time()
model.fit(x_train,y_train)
end_time = time.time()   


#4. 평가, 예측
y_predict = model.predict(x_test)
print("r2_score : ", r2_score(y_test, y_predict))
# r2_score :  0.8357082683009049

print("걸린시간 : ", round(end_time - start_time, 2), '초')
# 걸린시간 :  0.17 초


