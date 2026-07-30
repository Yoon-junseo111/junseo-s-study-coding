import tensorflow as tf  # tensorflow 가져오기
print(tf.__version__)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense         # Dense 레이어는 입력된 데이터의 특징들을 가중치(w)와 편향(b)을 이용해 섞고 요리하여 새로운 특징을 추출하거나(은닉층), 최종 예측값으로 변환(출력층)하는 딥러닝의 가장 핵심적인 일꾼
import numpy as np

#1. 데이터 (전처리)
x = np.array([1,2,3,4,5,6])  
y = np.array([1,2,3,4,5,6])

#2. 모델구성 # y=wx+b
model = Sequential() # 한 방향으로 차례대로 연결
model.add(Dense(400000, input_dim=1)) # 노드가 출력되는것 #1-4-3-2-3 구조  , input_dim 을 지워서 간결하게 가능
model.add(Dense(3))
model.add(Dense(2))
model.add(Dense(700000))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam') # 평균 제곱 오차(MSE)를 기준으로 얼마나 틀렸는지 계산하고, Adam 알고리즘을 사용해서 오차가 줄어들도록 모델의 가중치를 업데이트하며 학습하라.
model.fit(x, y , epochs = 100)  # 훈련횟수   

#4. 평가, 예측
loss = model.evaluate(x, y)  # 평가  # 최소의 loss를 구하는 것이 목표, 최적의 W(Weight)를 구한다 (무조건 암기)    # loss = 손실
print("loss = ", loss )
result = model.predict(np.array([7]))
print("7의 예측값 : ", result)



