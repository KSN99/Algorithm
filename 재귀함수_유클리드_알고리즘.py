"""유클리드 호제법으로 최대공약수 구하기"""
def gcd(x:int,y:int) -> int:
    """정숫값 x와 y의 최대 공약수 반환"""
    if y==0:
        return x
    else:
        return gcd(y,x %y)

if __name__ == '__main__':
    print('gcd 구하기')
    x=int(input())
    y=int(input())
    print(f'두 정숫값의 최대 공약수는 {gcd(x,y)}.')
