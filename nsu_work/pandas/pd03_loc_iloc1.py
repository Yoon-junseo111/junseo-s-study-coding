import pandas as pd
print(pd.__version__)   # 3.0.3

data = [
    ['삼성', '1000', '2000'],
    ['현대', '1100', '3000'],
    ['LG', '2000', '500'],
    ['아모레', '3500', '6000'],
    ['네이버', '100', '1500']
]
index = ['031', '059', '033', '045', '023']   # index = 횡 번호매기기
columns = ['종목명', '시가', '종가']

df = pd.DataFrame(data=data, index=index, columns=columns)   # df = 데이터프레임
print(df)
#      종목명    시가    종가
# 031   삼성  1000  2000
# 059   현대  1100  3000
# 033   LG  2000   500
# 045  아모레  3500  6000
# 023  네이버   100  1500

# print(data[0][1])   
#      종목명    시가    종가
# 031   삼성  1000  2000
# 059   현대  1100  3000
# 033   LG  2000   500
# 045  아모레  3500  6000
# 023  네이버   100  1500
# 1000


# print(df[0])   # KeyError(key) from err
# print(df['031']) # KeyError(key) from err
print(df['종목명'])                      # ★★★"판다스 열행"★★★, 컬럼,피처, 열이 기준
#      종목명    시가    종가
# 031   삼성  1000  2000
# 059   현대  1100  3000
# 033   LG  2000   500
# 045  아모레  3500  6000
# 023  네이버   100  1500
# 031     삼성
# 059     현대
# 033     LG
# 045    아모레
# 023    네이버
# Name: 종목명, dtype: str



######## 아모레 시가 출력 ########
# print(df[3, 1]) # error
# print(df[3][1]) # error
# print(df['045', '시가']) # error
# print(df[045][시가]) # error
# print(df[['045']['시가']]) # error    # 행렬 방식은 모두 에러

# print(df['시가','045']) # error
# print(df['시가']['045'])  # 3500    # ★★★"판다스 열행"★★★
# print(df[1, 3])  # error

###################################################################
 # loc : 인덱스 기준으로 행 데이터 추출
 # iloc : 행번호 기준으로 행 데이터 추출
 #        int loc 외우기

##########################################################################
print(df)
#      종목명    시가    종가
# 031   삼성  1000  2000
# 059   현대  1100  3000
# 033   LG  2000   500
# 045  아모레  3500  6000
# 023  네이버   100  1500
print("=======================================")
print(df.iloc[3])
# 종목명     아모레
# 시가     3500
# 종가     6000
# Name: 045, dtype: str

# print(df.iloc["045"])   # error
# print(df.iloc[3])   # error
print(df.loc["045"])  
# 종목명     아모레
# 시가     3500
# 종가     6000
# Name: 045, dtype: str

# index가 아닌 숫자만 넣어줘야 한다. int_location
print("네이버 뽑기")
print(df.iloc[4])
print(df.loc['023'])
# 네이버 뽑기
# 종목명     네이버
# 시가      100
# 종가     1500
# Name: 023, dtype: str

print("아모레 시가뽑기")
print(df.iloc[3, 1])
# 아모레 시가뽑기
# 3500
# print(df.iloc[3][1]) # error
# print(df.iloc[3, '시가'])  # error
print(df.iloc[3],['시가'])
# 3500
print(df.iloc[3].iloc[1])
# 3500
print(df.iloc[3].loc["시가"])
# 3500
print(df.loc['045'].loc['시가'])
# 3500
print(df.loc['045'].iloc[1])
# 3500

# iloc는 column 빼고 숫자만