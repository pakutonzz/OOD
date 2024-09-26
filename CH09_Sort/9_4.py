def insert(sorted_list, value):

    if len(sorted_list) == 0 or value >= sorted_list[-1]:
        return sorted_list + [value]
    else:
        return insert(sorted_list[:-1], value) + [sorted_list[-1]]

def find_median(sorted_list):
    n = len(sorted_list)
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : " + Ans)
else:
    l = list(map(int, l))
    sorted_list = []
    for i in range(len(l)):
        sorted_list = insert(sorted_list, l[i]) 
        median = find_median(sorted_list)
        print(f"list = {l[:i+1]} : median = {median:.1f}")