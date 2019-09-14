# Python 3.x
def min_heapify(arr, node_index):
    #print('Begining of index {} = {}'.format(node_index, arr))
    left = node_index * 2 + 1
    right = node_index * 2 + 2
    length = len(arr) - 1
    smallest = node_index
    if left <= length and arr[left] < arr[smallest]:
        smallest = left
    if right <= length and arr[right] < arr[smallest]:
        smallest = right
    if smallest != node_index:
        arr[node_index], arr[smallest] = arr[smallest], arr[node_index]
        min_heapify(arr, smallest)
    #print('End of index {} = {}'.format(node_index, arr))

def create_min_heap(arr):
    for i in reversed(range(len(arr)//2)):
        min_heapify(arr, i)

def heap_sort(arr):
    create_min_heap(arr)
    print('Result Heap = {}'.format(arr))
    
    res = []
    for _ in range(len(arr)):        
        arr[0], arr[-1] = arr[-1], arr[0]
        res.append(arr.pop())
        min_heapify(arr, 0)

    return res

i_p = [30,4,2,7,15,10,5]

sorted_res = heap_sort(i_p)
print("Sorted res = {}".format(sorted_res))
