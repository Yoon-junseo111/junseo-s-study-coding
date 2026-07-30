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
model.add(Dense(400000, input_dim=1)) # 노드가 출력되는것 #1-4-3-2-3 구조  , input_dim 을 지워서 간결하게 가능   # Dense n개의 노드 층을 만들겠다.
model.add(Dense(3))    # 1에서 있던 히든부분 input_dim 생략
model.add(Dense(2))
model.add(Dense(700000))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x, y , epochs = 100)  # 훈련횟수  

#4. 평가, 예측
result = model.predict(np.array([7]))
print("7의 예측값 : ", result)

# Git Hub 잔디밭 설치
# loss = 손실
