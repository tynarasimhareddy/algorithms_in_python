
def merge(arr, low, mid, high):
    temp = []
    i = low
    j = mid+1
    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= high:
        temp.append(arr[j])
        j += 1

    j = 0
    for i in range(low, high+1):
        arr[i] = temp[j]
        j += 1

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)


arr = [4, 2, 11, 9, 32, 15, 12, 7]
print('Input list - {}'.format(arr))

merge_sort(arr, 0, len(arr) - 1)

print('Sorted list - {}'.format(arr))
