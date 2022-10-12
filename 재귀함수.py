def hello(count):
    if count == 0:
        return
    print("Hello",count)
    
    count-=1
    hello(count)

hello(5)

#자기 자신을 계속해서 호출함.
#파이썬 최대 재귀 깊이 = 1000 