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

inp = input("Enter people : ")

MQ = queue()
Q1 = queue()
Q2 = queue()

t = 0
timeQ1 = 0 
timeQ2 = 0

for i in inp :
    MQ.put(i)


while not MQ.isEmpty() :

    if timeQ1 == 0 and not Q1.isEmpty() :
        Q1.dequeue()
        if not Q1.isEmpty() :
            timeQ1 = 2
    else :
        timeQ1 -= 1
    
    if timeQ2 == 0 and not Q2.isEmpty():
        Q2.dequeue()
        if not Q2.isEmpty() :
            timeQ2 = 1
    else :
        timeQ2 -= 1
    
    if not MQ.isEmpty() :
        if Q1.size() < 5 :
            Q1.put(MQ.dequeue())
            if Q1.size() == 1 :
                timeQ1 = 2
        elif Q2.size() < 5 :
            Q2.put(MQ.dequeue())
            if Q2.size() == 1 :
                timeQ2 = 1

    t += 1
    print(t, MQ, Q1, Q2)