# 18 카피

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score  # 다중 분류
from sklearn.datasets import load_digits
import numpy as np
import pandas as pd
import time

#1. 데이터
datasets = load_digits()
print(datasets)  
print(datasets.DESCR)
print(datasets.feature_names)

# exit() 
x = datasets.data
y = datasets.target
print(x)
print(y)

print(x.shape, y.shape)   # (1797, 64) (1797,)
print(np.unique(y, return_counts= True)) 
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 
# array([178, 182, 177, 183, 181, 182, 181, 179, 174, 180]

# exit()


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
model.add(Dense(60, activation='relu' , input_shape=(64, )))
model.add(Dense(33, activation='relu'))
model.add(Dense(22, activation='relu')) 
model.add(Dense(13, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='softmax'))


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

