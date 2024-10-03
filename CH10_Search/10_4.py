class HashTable:
    def __init__(self, size, max_col, threshold):
        self.size = size
        self.max_col = max_col
        self.threshold = threshold
        self.table = [None] * size
        self.data_count = 0
        self.add_list = set()

    def insert(self, key):
        index = key % self.size
        init_index = index
        col = 0

        while col < self.max_col:
            if self.table[index] is None:
                self.table[index] = key
                self.data_count += 1
                self.add_list.add(key)
                return True
            else:
                col += 1
                print(f"collision number {col} at {index}")
                if col >= self.max_col:
                    print("****** Max collision - Rehash !!! ******")
                    return False
                index = (init_index + col ** 2) % self.size
        return False

    def is_over(self):
        percent = (self.data_count + 1) / self.size * 100
        if percent >= self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            return True
        return False

    def rehash(self):
        self.size = self.get_prime(self.size * 2)
        self.table = [None] * self.size
        self.data_count = 0
        for key in self.add_list:
            self.insert(key)

    def get_prime(self, n):
        def is_prime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        prime = n
        while True:
            if is_prime(prime):
                return prime
            prime += 1

    def print_table(self):
        for i in range(self.size):
            value = self.table[i]
            print(f"#{i + 1}\t{value if value is not None else 'None'}")
        print("----------------------------------------")

    def add_data(self, key):
        print(f"Add : {key}")
        if self.is_over():
            self.rehash()
        inserted = self.insert(key)
        if not inserted:
            self.rehash()
            self.insert(key)
        self.print_table()



print(" ***** Rehashing *****")
inp = input("Enter Input : ").split('/')
table_info = list(map(int, inp[0].split()))
table_size = table_info[0]
max_collision = table_info[1]
threshold = table_info[2]
data = list(map(int, inp[1].split()))

hash_table = HashTable(table_size, max_collision, threshold)
print("Initial Table :")
hash_table.print_table()

for key in data:
    hash_table.add_data(key)