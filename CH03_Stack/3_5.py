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
    
    def remove(self, value):
        self.stack.remove(value)

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()

### Enter Your Code Here ###
m,n = int(m),int(n)

S = Stack()


for car in s.split(',') :
    if car is not '0':
        S.push(int(car))

if o == 'arrive' :
    if S.size() >= m :
        print(f'car {n} cannot arrive : Soi Full')
    elif n in S.stack :
        print(f'car {n} already in soi')
    else :
        S.push(n)
        print(f'car {n} arrive! : Add Car {n}')

if o == 'depart' :
    if S.size() == 0 :
        print(f'car {n} cannot depart : Soi Empty')
    elif n not in S.stack :
        print(f'car {n} cannot depart : Dont Have Car {n}')
    else :
        S.remove(n)
        print(f'car {n} depart ! : Car {n} was remove')
    

print(S.stack)