class Queue:
    def __init__(self):
        self.queue = []
    
    def put(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def __str__(self):
        return f"Queue: [{', '.join(f'({x}, {y})' for x, y in self.queue)}]"

def find_path(w, h, r):
    w, h = int(w), int(h)
    rooms = r.split(',')
    
    if len(rooms) != h or any(len(row) != w for row in rooms) or 'F' not in r:
        return -1
    
    Q = Queue()
    passed = set()

    for y, row in enumerate(rooms):
        for x, cell in enumerate(row):
            if cell == 'F':
                Q.put((x, y))
                passed.add((x, y))
                break
        if not Q.is_empty():
            break
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    while not Q.is_empty():
        print(Q)
        x, y = Q.dequeue()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in passed:
                if rooms[ny][nx] == 'O':
                    return 1
                if rooms[ny][nx] == '_':
                    Q.put((nx, ny))
                    passed.add((nx, ny))
    
    return 0

w, h, r = input('Enter width, height, and room: ').split(' ')
result = find_path(w, h, r)
if result == 1:
    print('Found the exit portal.')
elif result == 0:
    print('Cannot reach the exit portal.')
else:
    print('Invalid map input.')
