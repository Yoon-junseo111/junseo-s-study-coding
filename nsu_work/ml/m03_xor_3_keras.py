# 3 카피
# 다층퍼셉트론 구성으로 xor 인공지능 겨울 문제 해결
import numpy as np
from sklearn.svm import LinearSVC   #  모델 이름 = LinearSVC(단층 모델)
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


#1. 데이터
x_data = np.array([[0,0], [0,1], [1,0], [1,1]])
y_data = np.array([0,1,1,0])                     

print(x_data.shape, y_data.shape)  #  (4, 2) (4,)


#2. 모델
# model = LinearSVC()  # 로스 자체에 컴파일이 포홤되어있음
# model = Perceptron()
model = Sequential()
model.add(Dense(8, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


 
#3. 컴파일, 훈련

model.compile(loss='binary_crossentropy', optimizer = 'adam',
            metrics=['acc'])

model.fit(x_data, y_data, batch_size = 100, epochs = 300, )



#4. 평가, 예측
results=model.evaluate(x_data, y_data)
print("results : ", results)

y_predict = np.round (model.predict(x_data))

# results = model.score(x_data, y_data)    # 평가지표 : accuracy
# print(results)

acc = accuracy_score(y_data, y_predict)
print("acc : ", acc)   # acc :  0.5

# 인공지능 첫번째 겨울 해결방안 : 퍼셉트론

# 훈련을 많이할수록 acc이 올라간다