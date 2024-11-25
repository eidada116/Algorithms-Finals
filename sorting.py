import time

room_prices = [150, 200, 100, 75, 180, 120, 250, 220, 530,738,283,120,100]

def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


#sorting method
def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)

#actual merging
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

bubble_prices = room_prices.copy()  
start = time.time()
bubble_sort(bubble_prices)
bubble_time = time.time() - start

print("Bubble Sort Results:")
print(f"Bubble Sort runtime: {bubble_time} seconds")
print("Sorted Room Prices (Bubble Sort):", bubble_prices)

prices = room_prices.copy()  
start = time.time()
sorted_merge = merge_sort(prices)
merge_time = time.time() - start

print("\nMerge Sort Results:")
print(f"Merge Sort runtime: {merge_time} seconds")
print("Sorted Room Prices (Merge Sort):", sorted_merge)
