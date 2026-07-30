import tensorflow as tf
print(tf.__version__)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

#1. 데이터
x = np.array([1,2,3,4,5,6])  #
y = np.array([1,2,3,4,5,6])

#2. 모델구성 # y=wx+b
model = Sequential()
model.add(Dense(400000, input_dim=1)) # 노드가 출력되는것 #1-4-3-2-3 구조
model.add(Dense(3, input_dim=4))  
model.add(Dense(2, input_dim=700000))
model.add(Dense(700000, input_dim=2))
model.add(Dense(1, input_dim=3))  # 출력은 무조건 1개

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x, y , epochs = 100)  # 훈련횟수  

#4. 평가, 예측
result = model.predict(np.array([7]))
print("7의 예측값 : ", result)

# Git Hub 잔디밭 설치
# loss = 손실
# 두 개 이상은 list