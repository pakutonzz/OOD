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
    
    def __str__(self) :
        return str(self.queue)
    
def check_dup(l) :
    for i in l.queue :
        if l.queue.count(i) > 1 :
            return 1
    return 0
    
inp = input("Enter Input : ").split('/')

Q = queue()

for num in inp[0].split() :
    Q.put(num)

for i in inp[1].split(','):
    if 'E' in i :
        Q.put(i.split()[1])
    if 'D' in i :
        if not Q.isEmpty() :
            Q.dequeue()

if check_dup(Q) :
    print('Duplicate')
else :
    print('NO Duplicate')




