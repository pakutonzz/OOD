class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return str(self.queue)

def simulate_queue_processing(people):
    main_queue = Queue()
    cashier1_queue = Queue()
    cashier2_queue = Queue()
    
    for person in people:
        main_queue.enqueue(person)
    
    time = 0
    cashier1_time_left = 0
    cashier2_time_left = 0

    while not main_queue.is_empty() or not cashier1_queue.is_empty() or not cashier2_queue.is_empty():
        time += 1
        
        # Process cashier 1
        if cashier1_time_left > 0:
            cashier1_time_left -= 1
        if cashier1_time_left == 0 and not cashier1_queue.is_empty():
            cashier1_queue.dequeue()
            if not cashier1_queue.is_empty():
                cashier1_time_left = 2  # Reset cashier 1's time for the next customer

        # Process cashier 2
        if cashier2_time_left > 0:
            cashier2_time_left -= 1
        if cashier2_time_left == 0 and not cashier2_queue.is_empty():
            cashier2_queue.dequeue()
            if not cashier2_queue.is_empty():
                cashier2_time_left = 1  # Reset cashier 2's time for the next customer

        # Move customers to cashiers' queues
        if not main_queue.is_empty():
            if cashier1_queue.size() < 5:
                cashier1_queue.enqueue(main_queue.dequeue())
                if cashier1_queue.size() == 1:
                    cashier1_time_left = 2
            elif cashier2_queue.size() < 5:
                cashier2_queue.enqueue(main_queue.dequeue())
                if cashier2_queue.size() == 1:
                    cashier2_time_left = 1
        
        print(f"{time} {main_queue} {cashier1_queue} {cashier2_queue}")

# Input
people = list("Lorem_Ipsum")

# Simulate
simulate_queue_processing(people)