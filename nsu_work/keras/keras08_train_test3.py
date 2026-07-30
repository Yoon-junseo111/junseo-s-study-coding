import tensorflow as tf  # tensorflow 가져오기
print(tf.__version__)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection  import train_test_split    # 사이킷런 = train_test_split
import numpy as np # 수치 계산을 빠르고 편리하게 하기 위한 라이브러리

#1. 데이터 (전처리)
# x = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]]) # (2, 6)  # 두 개 이상은 list  # 데이터가 두 덩어리가 되었기 때문에 input_dim = 2 

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1,2,3,4,5,6,7,8,9,10])          

x_train, x_test, y_train, y_test = train_test_split(x,  y, 
                                     train_size = 0.7, 
                                     random_state = 168,)  # ramdom_state =  랜덤값이 바뀌어도 항상 동일한 값을 얻기위해 (랜덤결과값 고정)
                                     # shuffle=False )   # 데이터가 차례대로(순서대로) 나옴 # shuffle=true가 디폴트값      

#x_train = x[0:7] # 0 부터 6까지  # 수는 무조건 0부터 시작   # 7:3으로 슬라이싱 하기 
#x_test = x[7:10] # 마지막  카운트는 -1
                                                                  # train = 학습용, test = 평가용 으로 나눔
#y_train = x[:7] # 0 부터 6까지  # 수는 무조건 0부터 시작
#y_test = x[7:] # 마지막  카운트는 -1

print(x_train,x_test)
print(y_train,y_test)

# exit()
 

print(x_train.shape, x_test.shape)  # (7,) (3,)

 # print(y_train.shape, y_test.shape)  # (7,) (3,)
  
# exit()  # 작업 끊기


#2. 모델구성 # y=wx+b  w = weight b = bias  절편
model = Sequential() # 한 방향으로 차례대로 연결
# 예시 model.add(Dense(400000, input_dim=2)) # 입력값이 400000개인 데이터를 받아, 뉴런이 3개인 완전 연결층을 모델에 추가한다.  # shape = 4차원에서 주로사용, 실무에서 많이 사용 
model.add(Dense(200, input_shape=(1, ))) # 노드가 출력되는것 #1-4-3-2-3 구조  , input_dim 을 지워서 간결하게 가능
model.add(Dense(100)) 
model.add(Dense(100))
model.add(Dense(10))
model.add(Dense(1))                                                                                                                                          

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')   # mse = 오차계산, # adam = 가중치를 어떻게 수정할지 결정
model.fit(x_train, y_train , epochs = 100, ) 


#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print("loss = ", loss )
# result = model.predict(np.array([[7, 13]]))    
# print("7의 예측값 : ", result)  # (1, 2)
result = model.predict(np.array([11]))  #(1, 3)   # 열 맨뒤 숫자 표시  # 행무시, 열우선
print("11의 예측값 : ", result) # 11의 예측값 :  [[10.9512]]

# 행무시, 열우선 (중요)                                                                                                                                                    

