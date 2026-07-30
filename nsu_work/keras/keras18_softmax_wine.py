from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, root_mean_squared_error, mean_squared_error
from sklearn.datasets import load_breast_cancer, load_iris, load_wine
import time
import numpy as np
import pandas as pd

#1. 데이터
datasets = load_wine()
print(datasets)  
print(datasets.DESCR)
print(datasets.feature_names)

#exit() 
x = datasets.data
y = datasets.target
print(x)
print(y)

print(x.shape, y.shape)  
print(np.unique(y, return_counts= True))

exit()

########## Onehot 01 판다스 이용 ##########
# y = pd.get_dummies(y)     
# print(y)    

########## Onehot 02 Tensorflow 이용 #########
from tensorflow.keras.utils import to_categorical
y = to_categorical(y)
print(y)



x_train, x_test, y_train, y_test = train_test_split(
    x, y, 
    train_size = 0.75,      
    random_state = 333,   
    shuffle = True,
)
print(x_train.shape, x_test.shape)   # (15480, 8) (5160, 8)
print(y_train.shape, y_test.shape)   # (15480,) (5160,)
print(np.unique(y_train, return_counts= True))
# exit()

#2. 모델구성
model = Sequential()   
model.add(Dense(200, activation='relu' , input_shape=(4, )))
model.add(Dense(11, activation='relu')) 
model.add(Dense(33, activation='relu')) 
model.add(Dense(150, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(3, activation='softmax')) 

#3. 컴파일, 훈련        
from tensorflow.keras.callbacks import EarlyStopping 
es = EarlyStopping(
    monitor='val_loss',
    mode ='min',            # 'auto' 로 설정시 자동 
    patience=100,
    restore_best_weights = True, 
)

model.compile(loss = 'categorical_crossentropy', optimizer ='adam',
              metrics =['accuracy'],
              ) 
start_time = time.time()
model.fit(x_train, y_train, epochs = 30, verbose = 1,
          validation_split = 0.1,
          callbacks = [es],
          batch_size = 10000)   
end_time = time.time()

print("=========================")
#4. 평가, 예측  
loss = model.evaluate(x_test, y_test)   # 수치 낮으면 좋음
print("loss = ", loss)      
           
y_predict = model.predict(x_test)
print(y_predict)
y_predict = np.argmax(y_predict, axis=1)
print(y_predict)
y_test = np.argmax(y_test, axis=1)
print(y_test)

print("y_test의 원값 :", y_test, y_test.shape)
print("[x_test]의 예측값 : ", y_predict,y_predict.shape)

print("걸린시간 :", round(end_time - start_time, 2), "초")


from sklearn.metrics import accuracy_score
acc_score = accuracy_score(y_test, y_predict)
print('accuracy_score :', acc_score)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#|              |     회귀      |       이진분류       |         다중분류            |
#|ㅡㅡㅡㅡㅡㅡㅡ |ㅡㅡㅡㅡㅡㅡㅡ  |ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ |
#|     input    |   임의 갯수   |      임의 갯수       |          임의 갯수          |
#|ㅡㅡㅡㅡㅡㅡㅡ |ㅡㅡㅡㅡㅡㅡㅡ  |ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ |
#| 마지막 layer |     linear    |       Sigmoid        |         Softmax            | 
#| (activation) |     (선형)    |                      |                            |
#|ㅡㅡㅡㅡㅡㅡ   |ㅡㅡㅡㅡㅡㅡㅡ  |ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ |
#|   loss       |  mae , mse   |  binary_crossentropy | categorial_cross entropy   |
#|ㅡㅡㅡㅡㅡㅡㅡㅡ|ㅡㅡㅡㅡㅡㅡㅡ |ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ |
#| 마지막 layer  |   1개 이상    |          1          |        Class 갯수           | 
#| (node의 갯수) |              |                     |        (y값의 종류)          |  
#|ㅡㅡㅡㅡㅡㅡㅡ |ㅡㅡㅡㅡㅡㅡㅡ  |ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ |  
#|   OneHot     |      X       |           X          |  y_trian, y_test, y_val    |  
#| ㅡㅡㅡㅡㅡㅡㅡ| ㅡㅡㅡㅡㅡㅡㅡ  |ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ |ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ |
#|    avgmax    |      X       |           X          |             O              |
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 
#  binary_crossentropy : 0 ~ 1 사이 Sigmoid 값을 빼고 반올림

# 분류 : 이진(2개) : 0 or 1 찾는것 / 다중(2개이상)
# 이진 분류 : binary_crossentropy , Sigmoid 고정
# 데이터를 나누는 이유(train/test) : 과적합 방지

