# 11_2 카피
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,root_mean_squared_error,mean_squared_error
from sklearn.datasets import load_diabetes    # 당뇨병 
import time

#1. 데이터
datasets = load_diabetes ()    
print(datasets)
print(datasets.DESCR)   # 요약
print(datasets.feature_names)
# ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']


x = datasets.data
y = datasets.target
print(x)
print(y)

print(x.shape, y.shape)   # (442, 10) (442,)



x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    train_size=0.71,
    random_state= 42,
    shuffle=True)
    


print(x_train.shape, x_test.shape) # (331, 10) (111, 10)
print(y_train.shape, y_test.shape) # (331,) (111,)



#2. 모델
model=Sequential()
model.add(Dense(210, input_shape=(10, )))
model.add(Dense(100))
model.add(Dense(100))
model.add(Dense(10))
model.add(Dense(1))



#3. 컴파일, 훈련
model.compile(loss = "mse", optimizer = 'adam')
start_time =time.time()
model.fit(x_train, y_train, epochs = 100, verbose = 3, batch_size = 1000)   # 2.81초      
end_time = time.time()
# verbose = 0  : 훈련 과정 생략(침묵)
# verbose = 1  : 디폴트, 훈련 과정 나타남
# verbose = 2  : 진행 바(프로그래스 바,게이지) 생략
# verbose = 3이상  : 훈련 횟수(epoch)만 나타남


#4. 평가, 예측
# loss = model.evaluate(x_test, y_test)
# print("loss = ", loss)



model.predict(x_test)
y_predict = model.predict([x_test])
# print("y_test의 원값 :",y_test)
# print("[x_test]의 예측값: ", y_predict )

 
print("걸린시간 : ", round(end_time - start_time, 2), "초")   #3.09초