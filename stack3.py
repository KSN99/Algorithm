def find(self, value: Any) -> Any:
    """stack에서 value를 찾아 인덱스를 반환 (없으면 -1을 반환)"""
    for i in range(self,ptr -1,-1,-1): #꼭대기부터 선형검색
        if self.stk[i] == value:
            return i #search success
    return -1        #search fail

def count(self, value: Any) -> bool:
    """스택에 있는 value의 개수를 반환.
    """
    c=0
    for i in range(self.ptr): #바닥쪽부터 선형 검색
        if self.stk[i] == value:
            c +=1
    return c  

def __contains__(self, value:Any) -> bool:
    """스택에 value 가 있는지 판단"""
    return self.count(value)
def dump(self) -> None:
    """stack 안의 모든 데이터 바닥부터 꼭대기까지 출력"""
    if self.is_empty():
        print('stack is empty')
    else:
        print(self.stk[:self.ptr])