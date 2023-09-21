import pandas as pd

data = [] # 빈 데이터 list 생성
df = pd.DataFrame(data,
                  columns = ['순위', '이름', '잔액']) # 순위, 이름, 잔액 dataframe 생성

data_old = pd.read_csv('rankingdata.txt', sep='\t') # 이전 text파일에 있던 data 가져오기

df = pd.concat([df, data_old]) # df dataframe에 이전 데이터 넣기
