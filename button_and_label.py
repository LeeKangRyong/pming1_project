from tkinter import *
import graph_update as gu

## 초기 변수들 설정 ------------------------------------------- ##

coin_count = 0 # 보유 중인 코인 갯수
final_account = 0 # 최종 잔액
account = 100000000 # 초기 자본 : 1억
myaccount = 0 # 랭킹에 넣을 최종 잔액 값을 마지막에 받기 위해 변수 생성

loan = 20000000 # 1회 대출금액 : 3천만원
principle = 0 # 대출액(원금)
interest = 0.01 # 이자

# 타이머 시간 설정
end = 85 # 시작 시간 설정
start = 0 # 지난 시간
myTime = end - start # 남은 시간

## ----------------------------------------------------------- ##

gu.graph_update()  # 처음 코인 값 설정을 위해 그래프 함수 1회 실행

window = Tk() # 매도, 매수, 대출 버튼 및 코인 잔액, 남은 시간 등을 보여주는 창 생성 

window.title("매도매수") # 창 제목 설정

frame_button = Frame(window, relief=SOLID, bd=2) # button 위젯 넣을 frame 생성
frame_button.pack(side=LEFT, fill=BOTH, expand=True)

frame_label = Frame(window, relief=SOLID, bd=2) # label 위젯 넣을 frame 생성
frame_label.pack(side=RIGHT, fill=BOTH, expand=True)
## button의 함수들 설정 --------------------------------------------------- ##  
  
def sellFunc(): # 매도 버튼 함수
    global account, coin_count
    
    if coin_count == 0: # 코인 개수가 0개면 작동 X
        pass
    
    else:
        coin_count -= 1 # 버튼 클릭 시 코인 개수 1개 감소
        label_Coin['text'] = '코인 갯수 : ' + str(coin_count) # 코인 개수 label 변경
        account += gu.y_val[gu.time_v + 1] # 잔액에 현재 코인 값 더하기
        label_Account['text'] = '금액 : ' + str(round(account,0)) # 잔액 label 변경 
        
def buyFunc(): # 매수 버튼 함수
    global account, coin_count

    if gu.coin_price > account: # 코인 가격이 잔액보다 높으면 작동 X
        pass
            
    else:
        account -= gu.y_val[gu.time_v + 1] # 잔액에 코인 값 빼기
        label_Account['text'] = '금액 : ' + str(round(account,0)) # 잔액 label 변경

        coin_count += 1 # 코인 개수 1개 증가
        label_Coin['text'] = '코인 갯수 : ' + str(coin_count) # 코인 개수 label 변경

def all_sellFunc(): # 풀매도 함수(한번에 다 매도하기)
    global account, coin_count
        
    if coin_count == 0: # 코인 개수 0개면 작동 X
        pass
        
    else:
        account += coin_count * gu.y_val[gu.time_v + 1] # 잔액에 현재 코인값 X 가지고 있는 총 코인 개수 더하기
        label_Account['text'] = "금액 : " + str(round(account,0)) # 잔액 label 변경
        
        coin_count = 0 # 코인 개수 0개로 변경
        label_Coin['text'] = "코인 갯수 : " + str(coin_count) # 코인 개수 label 변경
        
def all_buyFunc(): # 풀매수 함수(한번에 다 매수하기)
    global account, coin_count
    
    if gu.coin_price > account: # 코인 가격이 잔액보다 높으면 작동 X
        pass
    
    else:
        all_coins = account // gu.y_val[gu.time_v + 1] # 구매할 총 코인 개수를 현재 코인 가격 기준 구하기
        account -= all_coins * gu.y_val[gu.time_v + 1] # 잔액에 현재 코인값 X 구매할 총 코인 개수 빼기
        label_Account['text'] = '금액 : ' + str(round(account,0)) # 잔액 label 변경
    
        coin_count += all_coins # 가지고 있는 코인 개수에 구매한 코인 개수 더하기
        label_Coin['text'] = '코인 갯수 : ' + str(coin_count)  # 코인 개수 label 변경
        
def loanFunc(): # 대출 버튼 함수
    global account, principle, loan
    account += loan # 버튼 클릭 시 1회 대출액 잔액에 더하기
    principle += loan # 대출금에 대출액 더하기
    label_Account['text'] = "금액 : " + str(round(account,0)) # 잔액 label 변경
    label_Loan['text'] = "대출금: " + str(principle) # 대출금 label 변경

def payoffFunc(): # 대출갚기 버튼 함수
    global account, principle, loan
    
    if principle <= loan: # 남은 대출금보다 갚을 대출액이 더 클 때 
        account -= principle # 잔액에서 남은 대출금 빼기
        principle = 0 # 대출금 0원으로 변경

    else:   
        account -= loan # 일반적으로 대출 갚으면 1회 대출금액을 갚음(잔액에서 대출액 빼기)
        principle -= loan # 대출금에서 대출액 빼기
        
    label_Account['text'] = "금액 : " + str(round(account,0)) # 잔액 label 변경
    label_Loan['text'] = "대출금: " + str(principle) # 대출금 label 변경

## ----------------------------------------------------------------------- ## 

# button 위젯    
button_Sell = Button(frame_button, text='매도', width=30, height=7, command=lambda: sellFunc(), bg='orange') 
button_Buy = Button(frame_button, text="매수", width=30, height=7, command=lambda: buyFunc(), bg='light blue')
button_all_Sell = Button(frame_button, width=30, height=7, text='풀매도', command=lambda: all_sellFunc(), bg='red')
button_all_Buy = Button(frame_button, width=30, height=7, text='풀매수', command=lambda: all_buyFunc(), bg='blue')
button_Loan = Button(frame_button, width=30, height=7, text='대출하기', command=lambda: loanFunc(), bg='green')
button_Payoff = Button(frame_button, width=30, height=7, text='대출금갚기', command=lambda: payoffFunc(), bg='light green')
# 매도, 매수, 풀매도, 풀매수, 대출, 대출갚기 button 생성 및 기능들 작성

# 각 button의 위치 설정 후 생성
button_Sell.grid(row=0, column=0)
button_Buy.grid(row=0, column=1)
button_all_Sell.grid(row=1, column=0)
button_all_Buy.grid(row=1, column=1)
button_Loan.grid(row=2, column=0)
button_Payoff.grid(row=2, column=1) 

# label 위젯
label_Explanation = Label(frame_label, text="가상코인체험기", font=("궁서체", 30), fg="blue") 
label_Account = Label(frame_label, text="잔액 : 100000000", bg='purple', width=20, height=5, anchor='center')
label_Coin = Label(frame_label, text='코인 갯수 : 0', fg='red', bg='white', borderwidth=3, relief='sunken', font=('궁서체', 20))
label_Loan = Label(frame_label, text="대출금: {}" .format(round(principle,2)))
label_Interest = Label(frame_label, text="이자 : {}%" .format(round(interest*100,2)))
# 설명, 잔액, 코인 개수, 대출금, 이자 label 생성 

# 각 label 위치 설정 후 생성
label_Explanation.pack()
label_Account.pack()
label_Coin.pack()
label_Loan.pack()
label_Interest.pack()
# (button, label들 예쁘게 정리할 것)

# 제한시간 함수 - 제한시간 구현 및 이자, 대출금 시간에 따라 상승하는 기능 구현
def time_Count():
    global myTime, end, start, interest, principle
    start += 1 # 1초가 지나 지난 시간에 1 더함
    myTime = end - start # 남은 시간 다시 설정
    timer.configure(text="남은 시간 : {} 초" .format(myTime)) # 제한시간 label 변경
    
    interest += 0.0005 # 1초마다 이자 상승
    label_Interest['text'] = "이자 : {} %" .format(round(interest*100,2)) # 이자 label 변경
    principle += principle*interest # principle 1초마다 복리로 상승
    label_Loan['text'] = "대출금: {}" .format(round(principle,0)) # 대출금 label 변경
    
    if myTime > 0:
        window.after(1000, time_Count) # 남은 시간이 0보다 크면, 1초(1000ms)후 제한시간 함수 작동

timer = Label(frame_label, text="남은 시간 : {} 초" .format(myTime)) # 제한시간 label 생성, 1초마다 함수가 작동해 값 변경
timer.pack() # 제한시간 label 위치 설정 및 생성

window.after(1000, time_Count) # 1초(1000ms)후 제한시간 함수 작동

while True: # 게임 시작
    gu.graph_update() # 그래프 함수 계속 반복 작동
    label_Interest['text'] = "이자 : {} %" .format(interest*100) # 이자 label 변경
    
    if myTime == 0:
        window.destroy()
        break # 제한시간 종료 시 break 하여 게임 종료
        
final_account = account + coin_count * gu.coin_price - principle # 잔액에서 남은 코인 개수 * 마지막 코인 가격과 대출금을 뺴 최종 잔액 도출 

# 모든 label의 값 표시에 round(x,0) 을 하여 실제 계산은 정확하지만, 편안하게 숫자를 보기 위해 소수점은 안보이게 설정함
    
myAccount = round(final_account,0) # final_account값 소수점 제외하여 가져감

window2 = Tk() # 두번째 창 생성(최종결과 설명)
window2.configure(bg='#f2f2f2')

Label(window2, text="남은 코인은 자동 매도되었습니다.").pack(pady=10)
Label(window2, text="(최종 잔액 = 잔액 + 남은 코인 - 대출금)").pack(pady=5)
Label(window2, text="최종 잔액: " + str(myAccount)).pack(pady=20)
Label(window2, text="이 창은 5초 후에 종료됩니다.").pack()

def close_window():
    window2.destroy() # 함수 작동 시 window2 종료

window2.after(5000, close_window) # 5초 있다가 close_window2() 실행 
window2.mainloop()