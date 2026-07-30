# 11_2 카피
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,root_mean_squared_error,mean_squared_error
from sklearn.datasets import load_breast_cancer    # 암 유무 
import time
import numpy as np

# 분류 : 이진 / 다중(3개 이상)

#1. 데이터
datasets = load_breast_cancer()    
print(datasets)
print(datasets.DESCR)   # 요약
print(datasets.feature_names)



x = datasets.data
y = datasets.target
print(x)
print(y)

print(x.shape, y.shape)   # (569, 30) (569,)
print(np.unique(y,return_counts=True))  #  (array([0, 1]), array([212, 357]))




x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    train_size=0.71,
    random_state= 42,
    shuffle=True)
    
print(x_train.shape, x_test.shape)  #(403, 30) (166, 30)
print(y_train.shape, y_test.shape)  #(403,) (166,)




#2. 모델구성
model=Sequential()
model.add(Dense(210,activation ='relu', input_shape=(30, )))
model.add(Dense(100,activation ='relu'))
model.add(Dense(100,activation ='relu'))
model.add(Dense(10,activation ='relu'))
model.add(Dense(1,activation ='sigmoid'))  

print(x_train.shape, y_train.shape)


# mse, mae, rmse, loss 등 은 linear



#3. 컴파일, 훈련
model.compile(loss = "binary_crossentropy", optimizer = 'adam',
              metrics=['accuracy',]   #  정확성,    
)  # 이진분류에서 binary_crossentropy는 무조건 sigmoid   , 이진분류 : 0이나 1이냐, A냐 B냐    Sigmoid는 0과 1 사이의 값이 나옴

from tensorflow.keras.callbacks import EarlyStopping 
es = EarlyStopping(
                    monitor = 'valid_loss',
                    mode = 'min',
                    patience = 100,
                    restore_best_weights = True)
start_time =time.time()
model.fit(x_train, y_train, epochs = 100, verbose = 1, batch_size = 1000,
          validation_split=0.1,
          callbacks = [es])   # 2.81초      
end_time = time.time()

print("================================")
# 4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print("loss = ", loss)   #  accuracy: 0.9096 - loss: 0.1718



model.predict(x_test)
y_predict = model.predict([x_test])
y_predict = np.round(y_predict)   # round = 소수점 첫째 자리 반올림
# print("y_test의 원값 :",y_test)
print("[x_test]의 예측값: ", y_predict )

 
print("걸린시간 : ", round(end_time - start_time, 2), "초")   #3.09초

from sklearn.metrics import accuracy_score
acc_score = accuracy_score(y_test, y_predict)
print('accuracy_score : ', acc_score)
# YOLO loss 에 대해 설명 가능해야됨 


# # 문제 유형	출력층 Activation	Loss
# 이진 분류	sigmoid	binary_crossentropy
# 멀티라벨 분류	sigmoid	binary_crossentropy
# 다중 클래스(하나만 정답)	softmax	categorical_crossentropy 또는 sparse_categorical_crossentropy
# 회귀	없음(linear)	mse, mae 등