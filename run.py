# name = str(input('사용자의 이름(닉네임)을 입력해주세요(4글자 이하): ')) # 사용자 이름 설정
from tkinter import *

name = "" # 사용자 이름 생성

def user_name():
    global name # name을 global 변수로 받아서 window창이 꺼진 뒤, 입력받은 name_entry 저장
    name = name_entry.get()
    window.destroy() # 확인 버튼 누르면 창 꺼지고, 게임 시작됨

window = Tk()
window.title("이름 입력")

Label(text='사용자의 이름을 입력해주세요.').pack(pady=10)
name_entry = Entry(window)   
name_entry.pack() # 사용자 이름 입력 Entry

Button(text='확인', command=user_name).pack(pady=10) # 이름 입력 후 확인 버튼 누르기
window.mainloop()

from button_and_label import * # button_and_label.py 작동(tkiner창 파일 실행)

import rankingdata # rankingdata.py 작동(랭킹 불러오기 파일 실행)

new_data = ['1', name, myAccount] # [순위, 사용자 이름, 최종 잔액] list 생성

df = rankingdata.df # rankingdata의 df
n_index = df.shape[0] # 새 list를 넣을 행 추가, 그 행의 index값 받아오기
df.loc[n_index] = new_data # 추가한 행에 새 list 넣기

df_sort = df.sort_values('잔액', ascending=False) # 잔액 기준 오름차순으로 데이터 정렬

for i in range(len(df_sort)):
    df_sort['순위'].values[i] = i + 1 # 순위 value에 i+1을 넣어 순위 지정(1위, 2위, 3위, ...)

#print(df_sort[n_index])    
df_sort.to_csv('rankingdata.txt',sep='\t', index=None) # tab 간격으로 띄워서 text 파일 생성

import showhtml # txt파일 html로 띄우는 파일 실행