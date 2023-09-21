import matplotlib.pyplot as plt
import random

x = 0
y = 0
time_v = 0
x_val=[0]
y_val=[0]
coin_price = 0 # coin 가격

def graph_update():    
    
    global x # global 변수로 받아야 함
    
    x += 1
    
    # x값에 따라 y값(코인 가격) 정하기
    
    # PART1 100만원 -> 500만원
    if x == 1:  y = 1000000
    elif x == 2:    y = 3000000
    elif x == 3:    y = 5000000
    # PART2 500만원 -> 2800만원
    elif x == 4:    y = 5000000
    elif x == 5:    y = 7000000
    elif x == 6:    y = 10000000
    elif x == 7:    y = 12000000
    elif x == 8:    y = 15000000
    elif x == 9:    y = 20000000
    elif x == 10:   y = 25000000
    elif x == 11:   y = 28000000
    # PART3 2800만원 -> 500만원
    elif x == 12:   y = 28000000
    elif x == 13:   y = 27000000
    elif x == 14:   y = 20000000
    elif x == 15:   y = 16000000
    elif x == 16:   y = 14000000
    elif x == 17:   y = 13000000
    elif x == 18:   y = 10000000
    elif x == 19:   y = 5000000
    # PART4 500만원 -> 600만원 -> 500만원
    elif x == 20:   y = 5000000
    elif x == 21:   y = 5500000
    elif x == 22:   y = 5700000
    elif x == 23:   y = 6000000
    elif x == 24:   y = 5500000
    elif x == 25:   y = 5000000
    # PART5 500만원 -> 100만원
    elif x == 26:   y = 5000000
    elif x == 27:   y = 4000000
    elif x == 28:   y = 1000000
    # PART6 100만원 -> 120만원
    elif x == 29:   y = 1000000
    elif x == 30:   y = 1100000
    elif x == 31:   y = 1200000
    # PART7 200만원 -> 1100만원
    elif x == 32:   y = 2000000
    elif x == 33:   y = 4000000
    elif x == 34:   y = 7000000
    elif x == 35:   y = 10000000
    elif x == 36:   y = 11000000
    # PART8 1100만원 -> 300만원, 400만원
    elif x == 37:   y = 8000000
    elif x == 38:   y = 7000000
    elif x == 39:   y = 3000000
    elif x == 40:   y = 4000000
    
    else:
        # 400만원 고정(남은 시간동안 가격 고정)
        y = 4000000
        
    x_val.append(x)
    y_val.append(y)
    
    plt.plot(x_val, y_val)
    for i, v in enumerate(x_val):
        plt.text(v, y_val[i], int(y_val[i]/10000)) # y_val(코인값) 표시(가격을 편하게 보기 위해 가격 줄여서 보이게 하기)
    plt.xlabel("Day")
    plt.ylabel("Price (x 10000 Won)")
    plt.show(block=False)
    plt.pause(2) # 2초동안 화면 고정
    
    global time_v
    global coin_price
    time_v += 1
    coin_price = y_val[time_v] # 매도, 매수 시 코인 가격 +/- => time_v 시점을 coin_price 변경 예정
    plt.close() # 2초동안 plot 띄운 뒤, 끔

# plot이 꺼지기 전에 time 변수를 +1 씩 하여 버튼을 누르면, y_val[time변수]를 추출