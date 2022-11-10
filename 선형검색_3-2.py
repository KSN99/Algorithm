#for문으로 작성한 선형 검색 알고리즘
#while 문과 비교해 배열의 스캔을 for문으로 구현하면 코드가 더 짧고 간결해짐.

from typing import Any,Sequence

def seq_search(a:Sequence, key:Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형검색"""
    for i in range(len(a)):
        if a[i] == key:
            return i
        return -1 