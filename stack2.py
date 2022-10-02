#고정 길이 스택 클래스 FixedStack 구현
from typing import Any
class FixedStack: 
    """고정 길이 스택 클래스"""
    class Empty(Exception):
        pass 
    """비어있는 FixedStack에 팝 또는 피크할 떄 내보내는 예외처리"""

    class Full(Exception):
        """"가득 찬 FixedClass에 푸시할 때 내보내는 예외 처리"""
        pass

    def __init__(self, capacity:int = 256) ->None:
        """스택 초기화"""
        self.stk = [None] * capacity #stack 본체
        self.capacity = capacity #stack 의 크기
        self.ptr=0 # stack pointer
    
    def __len__(self) ->int:
        """스택에 쌓여 있는 데이터 개수를 반환"""
        return self.ptr
    
    def is_empty(self) -> bool:
        """스택이 비어있는지 판단"""
        return self.ptr <=0
    def is_full(self) -> bool:
        """스택이 가득 차 있는지"""
        return self.ptr >=self.capacity