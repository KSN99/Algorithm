#for문으로 작성한 선형 검색 알고리즘
#while 문과 비교해 배열의 스캔을 for문으로 구현하면 코드가 더 짧고 간결해짐.

from typing import Any,Sequence

def seq_search(a:Sequence, key:Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형검색"""
    for i in range(len(a)):
        if a[i] == key:
            return i
        return -1 


num = int(input('원소 수를 입력하세요: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

ky= int(input('검색할 값: ')) #검색할 ky를 입력받음

idx = seq_search(x,ky) # ky와 값이 같은 원소를 x에서 검색

if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 x[{idx}]에 있습니다.')