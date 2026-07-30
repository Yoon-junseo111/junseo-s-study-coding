# 11_2 을 es 적용해서 성능향상해볼것
import warnings
warnings.filterwarnings("ignore") 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,root_mean_squared_error,mean_squared_error
from sklearn.datasets import load_diabetes    # 당뇨병 
import pandas as pd
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

print(x.shape, y.shape) 

print("==================================")





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

print (x_train.shape, y_train.shape)


start_time = time.time()
model.compile(loss = "mse", optimizer = 'adam')
from tensorflow.keras.callbacks import EarlyStopping 
es = EarlyStopping(
                    monitor = 'valid_loss',
                    mode = 'min',
                    patience = 100,
                    restore_best_weights = True)
                    
end_time = time.time()
                    
                    

model.fit(x_train, y_train, epochs = 100, batch_size = 1000, validation_split = 0.2, callbacks = [es])

loss = model.evaluate(x_test, y_test)
print("loss = ", loss)

model.predict(x_test)
y_predict = model.predict([x_test])
print("y_test의 원값 :",y_test)
print("[x_test]의 예측값: ", y_predict )


          
print("걸린시간 : ", round(end_time - start_time, 2), "초") 



from sklearn.metrics import r2_score, root_mean_squared_error, mean_absolute_error, mean_squared_error   # root_mean_squared_error = RMSE ,   mean_absolute_error = MAE


rmse = root_mean_squared_error(y_test, y_predict)
print("rmse : ", rmse)

