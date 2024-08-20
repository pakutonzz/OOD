class queue :
    def __init__(self) -> None:
        self.queue = []
    
    def put(self, value) :
        self.queue.append(value)

    def dequeue(self) :
         return self.queue.pop(0)
    
    def size(self) :
        return len(self.queue)
    
    def isEmpty(self) :
        return self.size() == 0

Q = queue()
DQ = queue()

inp = input('Enter Input : ').split(',')

def formatted_print(s) :
    if s.isEmpty() :
        return 'Empty'
    else :
        return ', '.join(map(str, list(s.queue)))

for i in inp :
    if 'E' in i :
        temp = i.split()
        Q.put(temp[1])
        print(formatted_print(Q))

    if 'D' in i :
        if Q.isEmpty() :
            print('Empty')
        else :
            DQ.put(Q.queue[0])
            Q.dequeue()
            print(f"{DQ.queue[-1]} <- {formatted_print(Q)}")
        
print(f"{formatted_print(DQ)} : {formatted_print(Q)}")