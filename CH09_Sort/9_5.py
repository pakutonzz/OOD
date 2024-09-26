def subset_sum(arr, target):
    result = set()

    def find_subsets(index, current_subset, current_sum):
        if current_sum == target:
            result.add(tuple(current_subset))
        if index == len(arr):
            return
        
        find_subsets(index + 1, current_subset + [arr[index]], current_sum + arr[index])
        find_subsets(index + 1, current_subset, current_sum)

    find_subsets(0, [], 0)
    return list(result)

def sort_subset(arr):
    return sorted(arr, key=lambda x: (len(x), x))

input_data = input("Enter Input : ").split("/")
target_sum = int(input_data[0])
arr = list(map(int, input_data[1].split()))

subsets = subset_sum(arr, target_sum)

sorted_subsets = [sorted(subset) for subset in subsets]

sorted_subsets = sort_subset(sorted_subsets)

if sorted_subsets:
    for subset in sorted_subsets:
        print(subset)
else:
    print("No Subset")
