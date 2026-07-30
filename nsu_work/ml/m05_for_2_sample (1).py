import numpy as np
from sklearn.datasets import load_iris, load_breast_cancer, load_wine
from sklearn.svm import LinearSVC 
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import warnings
warnings.filterwarnings("ignore")


#1. 데이터
data_list = [
    load_iris(return_X_y=True),
    load_breast_cancer(return_X_y=True),
    load_wine(return_X_y=True),
]

model_list = [
    LinearSVC(),
    LogisticRegression(),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
]

data_name_list =['아이리스 :', '브래스트캔서 :', '와인 :']
model_name_list = ['LinearSVC :', "LogisticRegreesion :",
                   'DecisionTree :', 'RF :']

#2. 모델
for i, value in enumerate(data_list):
    x, y = value
    print(x.shape, y.shape)
    print("==============================")
    print(data_name_list[i])
    
    for j, value2 in enumerate(model_list):
        model = value2
        
        #3. 컴파일 훈련
        model.fit(x,y)
        
        #4. 평가, 예측
        results = model.score(x,y) 
        print(model_name_list[j], "model.score :", results)
        
exit()

x,y = fetch_california_housing(return_X_y=True)
print(x.shape, y.shape)              # (20640, 8) (20640,)
           
#2. 모델구성


# model = LinearSVC()                      # 분류라 안됨
# model = LogisticRegression()             # 분류라 안됨
# model = DecisionTreeRegressor()          # 1.0        # 결정 트리 
model = RandomForestRegressor()            # 0.9744070898240709


#3. 컴파일, 훈련
model.fit(x,y)


#4. 평가, 예측
results = model.score(x,y)
print(results)



# Dicision forest VS Random Forest  →  Random Forest  
