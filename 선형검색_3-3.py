#linear_search() 함수를 사용하여 실수 검색

from 선형검색_3_1 import seq_search

print('실수를 검색')
print('Warning: If you put "end" program will be ended')

number = 0
x=[]  #빈리스트 생성

while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s)) #배열 맨끝에 원소를 추가 
    number +=1

ky=float(input('검색할 값을 입력: ')) #검색할 키 ky를 입력받기

idx = seq_search(x,ky)
if idx==-1:
    print('The key does not exsit')
else:
    print(f'The key is x[{idx}]')