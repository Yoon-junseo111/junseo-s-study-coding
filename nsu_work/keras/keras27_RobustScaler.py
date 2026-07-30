
# 26 카피

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,root_mean_squared_error,mean_squared_error
from sklearn.datasets import load_diabetes    # 당뇨병 
from sklearn.preprocessing import RobustScaler
import numpy as np



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

#scaler = MinMaxScaler()
# scaler = StandardScaler()
scaler = RobustScaler()

# scaler.fit(x_train)
# x_train = scaler.transform(x_train)

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
print(np.min(x_train), np.max(x_train))  # 0.0 1.0
print(np.min(x_test), np.max(x_test))    # 0.0 1.0



#2. 모델
model=Sequential()
model.add(Dense(210, input_shape=(10, )))
model.add(Dense(100))
model.add(Dense(100))
model.add(Dense(10))
model.add(Dense(1))

model.compile(loss = "mse", optimizer = 'adam')
model.fit(x_train, y_train, epochs = 100, batch_size = 1000)

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

# r2 score가 1에 가까울수록 정확

"""
train_size=0.8,
random_state=21
epochs = 100
batch_size = 50
r2_score : 0.4136692910320341

"""
"""
train_size=0.71,
random_state= 120
model=Sequential()
model.add(Dense(350, input_shape=(10, )))
model.add(Dense(120))
model.add(Dense(111))
model.add(Dense(10))
model.add(Dense(1))
0.505262818998891
"""