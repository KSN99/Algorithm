#거스름돈을 구하는 문제
#거스름돈 N원
#500,100, 50,10 원으로 최소 개수로 !

N = int(input())
count = 0

coin_types=[500,100,50,10]

for coin in coin_types:
    count += N//coin
    N %=coin

print(count)