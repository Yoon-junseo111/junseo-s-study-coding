from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,root_mean_squared_error,mean_squared_error
from sklearn.datasets import fetch_california_housing    # 캘리포니아의 주택 가격 


#1. 데이터
datasets = fetch_california_housing()    
print(datasets)
print(datasets.DESCR)   # 요약
print(datasets.feature_names)
# ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms'], 
# ['Population', 'AveOccup', 'Latitude', 'Longitude']


x = datasets.data
y = datasets.target
print(x)
print(y)

print(x.shape, y.shape)   # (20640, 8) (20640,)

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    train_size=0.85,
    random_state= 42,
    shuffle=True)
    


print(x_train.shape, x_test.shape) # (15480, 8) (5160, 8)
print(y_train.shape, y_test.shape) # (15480,) (5160,)


#2. 모델
model=Sequential()
model.add(Dense(400, input_shape=(8, )))
model.add(Dense(300))
model.add(Dense(100))
model.add(Dense(100))
model.add(Dense(1))

model.compile(loss = "mse", optimizer = 'adam')
model.fit(x_train, y_train, epochs = 1000, batch_size = 1000)

loss = model.evaluate(x_test, y_test)
print("loss = ", loss)

model.predict(x_test)
y_predict = model.predict([x_test])
print("y_test의 원값 :",y_test)
print("[x_test]의 예측값: ", y_predict )

from sklearn.metrics import r2_score, root_mean_squared_error, mean_absolute_error, mean_squared_error   # root_mean_squared_error = RMSE ,   mean_absolute_error = MAE
r2 = r2_score(y_test, y_predict)
print("r2_score :", r2)

rmse = root_mean_squared_error(y_test, y_predict)
print("rmse : ", rmse)

mse = mean_squared_error(y_test, y_predict)
print("mse :", mse)



"""
train_size=0.8,
random_state=21
epochs = 100
batch_size = 50
r2_score : 0.4136692910320341

"""

