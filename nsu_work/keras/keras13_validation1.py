# 11-3 카피

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,root_mean_squared_error,mean_squared_error
from sklearn.datasets import load_diabetes
import pandas as pd 
import time 



#1. 데이터
path = "./_data/"   # 경로 지정


train_csv = pd.read_csv(path + "train.csv", index_col=0)  # 자료 읽기  # index_col = 0 첫번째열 인덱스 사용
test_csv = pd.read_csv(path + "test.csv", index_col=0)  
submit_csv = pd.read_csv(path + "sampleSubmission.csv", index_col=0)
# print(train_csv) 
# print(train_csv.shape)    #  (10886, 12)
# print(test_csv)
# print(test_csv.shape)  # (6493, 8)
# print(submit_csv)
# print(submit_csv.shape)  # (6493, 1)

print(train_csv.columns) 
# Index(['season', 'holiday', 'workingday', 'weather', 'temp', 'atemp', 'humidity', 'windspeed', 'casual', 'registered', 'count',])
      

x = train_csv.drop(['casual', 'registered', 'count'],axis=1)    #  drop = 제거
                                                                #  axis=0 : 세로 방향(행) 을 기준으로 작업
                                                                #  axis=1 : 가로 방향(열) 을 기준으로 작업
                                                                #  y = count
print(x) #  [10886 rows x 8 columns]

print("==================================")

y = train_csv['count']
print(y)
print(y.shape)   # (10886,) 

x_train, x_test, y_train, y_test = train_test_split(     # 데이터 자르기
    x, y,
    train_size=0.7,
    random_state= 42,
    shuffle=True)
    

print(x_train.shape, x_test.shape)  # (7729, 8) (3157, 8)
print(y_train.shape, y_test.shape)  # (7729,) (3157,)



#2. 모델
model=Sequential()
model.add(Dense(500, activation ='relu',input_shape=(8, )))     # activation = 'relu' -> 활성화 함수 설정
model.add(Dense(400,activation ='relu'))           
model.add(Dense(300,activation ='relu'))
model.add(Dense(200,activation ='relu'))
model.add(Dense(100,activation ='relu'))
model.add(Dense(500,activation ='relu'))
model.add(Dense(300,activation ='relu'))
model.add(Dense(1,activation ='relu'))
model.add(Dense(1,activation ='linear'))     # linear = 입력값 그대로 출력하는 활성화 함수


print (x_train.shape, y_train.shape) # (7729, 8) (7729,)

model.compile(loss = "mse", optimizer = 'adam')
start_time = time.time()   # 시작 시간
model.fit(x_train, y_train, epochs = 100, batch_size = 1000, validation_split = 0.2)
#  validation = 학습 데이터(train data)의 일부를 자동으로 검증 데이터(validation data)로 나누는 옵션, 검증 데이터로 성능 확인 (문제점 : 과적합)
end_time = time.time()     # 끝난 시간

loss = model.evaluate(x_test, y_test)
print("loss = ", loss)

model.predict(x_test)
y_predict = model.predict([x_test])
print("y_test의 원값 :",y_test)
print("[x_test]의 예측값: ", y_predict )

from sklearn.metrics import r2_score, root_mean_squared_error, mean_absolute_error, mean_squared_error  

rmse = root_mean_squared_error(y_test, y_predict)
print("rmse : ", rmse)    #  rmse :  155.71661376953125


################# csv 파일 만들기 ########################

y_submit = model.predict(test_csv)             #   submit 파일에 test 파일 넣기
# print(y_submit)
submit_csv['count'] = y_submit                 #   count 열에 y_submit 값을 넣기
# print(submit_csv)
submit_csv.to_csv(path + "submission_2026_0717.csv")            #  7월 17일 
print("걸린시간 : ", round(end_time - start_time, 2), "초")     # 시간 나타내기

# R2 score를 제외한 나머지 rmse, mae 등은 낮아야 좋음 이유: loss값이 낮아야 되기 때문


# train, test 분리 이유 : 과적합 방지, 자료 정리 잘됨

