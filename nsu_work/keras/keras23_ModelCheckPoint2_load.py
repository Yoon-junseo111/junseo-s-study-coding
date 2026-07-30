# 23-1 카피

from tensorflow.keras.models import Sequential, load_model
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
# model=Sequential()
# model.add(Dense(5000, activation ='relu',input_shape=(8, )))     # activation = 'relu' -> 활성화 함수 설정
# model.add(Dense(4000,activation ='relu'))           
# model.add(Dense(3000,activation ='relu'))
# model.add(Dense(2000,activation ='relu'))
# model.add(Dense(1000,activation ='relu'))
# model.add(Dense(500,activation ='relu'))
# model.add(Dense(300,activation ='relu'))
# model.add(Dense(1,activation ='relu'))
# model.add(Dense(1,activation ='linear'))   


print (x_train.shape, y_train.shape) # (7729, 8) (7729,)


#3.  컴파일 , 훈련
######################################################################################
model = load_model('./_save/keras23_mcp1.keras')  # rmse :  262.23468017578125
######################################################################################

#4.  평가, 예측
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
submit_csv.to_csv(path + "submission_2026_0717.csv")            # 7월 17일 
# print("걸린시간 : ", round(end_time - start_time, 2), "초")     # 시간 나타내기

# R2 score를 제외한 나머지 rmse, mae 등은 낮아야 좋음, 이유: loss값이 낮아야 되기 때문


# train, test 분리 이유 : 과적합 방지, 자료 정리 잘됨

# rmse :  148.88671875   # 23-1에서 훈련을 했기 때문에 값이 똑같음