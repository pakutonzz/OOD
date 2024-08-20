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

activity = ['Eat', 'Game', 'Learn', 'Movie']
place = ['Res.', 'ClassR.', 'SuperM.', 'Home']

mq = queue()
yq = queue()

score = 0

inp = input('Enter Input : ')

for i in inp.split(',') :
    mq.put(i.split()[0])
    yq.put(i.split()[1])


print('My   Queue =',', '.join(mq.queue))
print('Your Queue =',', '.join(yq.queue))

mpl = []
ypl = []

while not mq.isEmpty() :
    ma, mp = mq.dequeue().split(':')
    ya, yp = yq.dequeue().split(':')
    mpl.append(f"{activity[int(ma)]}:{place[int(mp)]}")
    ypl.append(f"{activity[int(ya)]}:{place[int(yp)]}")
    if ma == ya and mp != yp :
        score += 1
    elif ma != ya and mp == yp :
        score += 2
    elif ma == ya and mp == yp :
        score += 4
    else :
        score -= 5

print("My   Activity:Location =", ', '.join(mpl))
print("Your Activity:Location =", ', '.join(ypl))

if score >= 7:
    print(f"Yes! You're my love! : Score is {score}.")
elif 0 < score < 7:
    print(f"Umm.. It's complicated relationship! : Score is {score}.")
else:
    print(f"No! We're just friends. : Score is {score}.")





