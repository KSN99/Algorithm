class Stack:
    def __init__(self):
        self.items= [] #데이터 저장ㅇ을 위한 리스트
    
    def push(self , val):
        self.items.append(val)
    
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:          #pop할 아이템이 없으면 indexerror 발생. 
            print("Stack is empty")
    
    def top(self):
        try:
            return self.items[-1]
        except ImportError:
            print("Stack is empty")
    def __len__(self):          #len()로 호출하면 stack의 item수 반환 
        return len(self.items)