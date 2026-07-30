import tensorflow as tf  # tensorflow 가져오기
print(tf.__version__)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np # 수치 계산을 빠르고 편리하게 하기 위한 라이브러리

#1. 데이터 (전처리)
# x = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]]) # (2, 6)  # 두 개 이상은 list  # 데이터가 두 덩어리가 되었기 때문에 input_dim = 2 

x = np.array([[1,2,3,4,5,6,7,8,9,10],
              [1,1.1,1.2,1.3,1.4,1.5,1.6,1.5,1.4,1.3],
              [9,8,7,6,5,4,3,2,1,0]]) 
# x = np.array([[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]) # (6, 2)
# x = x.T
x = x.transpose()  # 행과 열이 잘못되면 transpose 또는 T를 사용
print(x.shape)  # (10, 3)
y = np.array([[1,2,3,4,5,6,7,8,9,10],
             [9,8,7,6,5,4,3,2,1,0]]) 
y = y.transpose()
print(y.shape) #(10, 2)
 

# y = np.array([1,2,3,4,5,6,7,8,9,10])   # (6, )  # 열, column , feature, 특성, 속성, attribute 다 동일한 의미  # 1차원에서는 '1' 생략 가능

#2. 모델구성 # y=wx+b  w = weight b = bias  절편
model = Sequential() # 한 방향으로 차례대로 연결
# 예시 model.add(Dense(400000, input_dim=2)) # 입력값이 400000개인 데이터를 받아, 뉴런이 3개인 완전 연결층을 모델에 추가한다.  # shape = 4차원에서 주로사용, 실무에서 많이 사용 
model.add(Dense(200, input_dim=3)) # 노드가 출력되는것 #1-4-3-2-3 구조  , input_dim 을 지워서 간결하게 가능
model.add(Dense(100, input_shape=(3, ))) 
model.add(Dense(100))
model.add(Dense(10))
model.add(Dense(1))                                                                                                                                          

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')   # 평균 제곱 오차(MSE)를 기준으로 얼마나 틀렸는지 계산하고, Adam 알고리즘을 사용해서 오차가 줄어들도록 모델의 가중치를 업데이트하며 학습하라.
model.fit(x, y , epochs = 100, batch_size=4)  # 훈련횟수   # batch_size = 한 번에 모델이 학습하는 데이터의 개수, 훈련이  빨리지는 효과

#4. 평가, 예측
loss = model.evaluate(x, y)   # 평가  # 최소의 loss를 구하는 것이 목표, 최적의 W(Weight)를 구한다 (무조건 암기)    # loss = 손실
print("loss = ", loss )
# result = model.predict(np.array([[7, 13]]))   
# print("7의 예측값 : ", result)  # (1, 2)
result = model.predict(np.array([[10, 1.3, 0]]))  #(1, 3)   # 열 맨뒤 숫자 표시  # 행무시, 열우선
print("[[10, 1.3, 0]]의 예측값 : ", result) 

# 행무시, 열우선 (중요)                                                                                                                                                    

