class Stack:
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return len(self.item)==0
    def push(self,item):
        self.item.append(item)
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            item=self.item[-1]
            del(self.item[-1])
            print("the poped item is :",item)
    def display(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            for i in reversed(self.item):
                print(i)
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print("top item is :",self.item[-1])
S=Stack()
while(True):
    print("1:push 2: pop 3: display 4: peek 5:exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        item=input("enter the item to push")
        S.push(item)
    elif choice==2:
        S.pop()
    elif choice==3:
        S.display()
    elif choice==4:
        S.peek()
    else:
            break
            