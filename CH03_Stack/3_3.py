class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def size(self) :
        return len(self.stack)

    def isEmpty(self):
        return self.size() == 0

    

inp = input('Enter Infix : ')

S = Stack()
print('Postfix : ', end='')
### Enter Your Code Here ###
def priority(o): 
    if o == '+' or o == '-':
        return 1
    elif o == '*' or o == '/':
        return 2
    elif o == '^' :
        return 3
    return 0

for i in inp :
    if i == '(':
        S.push(i)
    elif i == ')' :
        while S.size() > 0 and S.stack[-1] != '(':
            print(S.pop(), end='')
        S.pop()
    elif i in '+-*/^':
        while S.size() > 0 and priority(S.stack[-1]) >= priority(i):
            print(S.pop(), end='')
        S.push(i)
    else :
        print(i, end='')

while not S.isEmpty():
    
    print(S.pop(), end='')


print()