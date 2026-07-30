# 10_1 카피
# load_breaste_cancer = 분류

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.model_selection import StratifiedKFold,GridSearchCV,RandomizedSearchCV
from sklearn.datasets import load_iris, load_breast_cancer
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import r2_score, accuracy_score
from xgboost import XGBClassifier
import time
from sklearn.decomposition import PCA
    

#1. 데이터
x, y = load_breast_cancer(return_X_y=True)

pca = PCA(n_components=10)
x = pca.fit_transform(x)                        # fit_transform = 전처리
print(x.shape)    # (569, 10)

exit()


x_train, x_test, y_train, y_test = train_test_split(
    x, y, shuffle=True, random_state=333, train_size=0.8,
    stratify=y                                                  
)
print(x_train.shape, x_test.shape) # (455, 30) (114, 30)
print(y_train.shape, y_test.shape) # (455,) (114,)


   
#2. 모델
parameters = {    
    "learning_rate" : 0.1,
    "max_depth": 6,
    "n_estimators" : 200,
}
  
   
  
model = XGBClassifier(**parameters)


#3. 컴파일, 훈련
start_time = time.time()
model.fit(x_train,y_train)
end_time = time.time()   


#4. 평가, 예측
print('model.score : ', model.score(x_test, y_test))
# model.score :  0.9912280701754386

y_predict = model.predict(x_test)
print("acc_score : ", accuracy_score(y_test, y_predict))
# acc_score :  0.9912280701754386

print("걸린시간 : ", round(end_time - start_time, 2), '초')
# 걸린시간 :  0.13 초





