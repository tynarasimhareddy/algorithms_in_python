def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot)
        quick_sort(arr, pivot+1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low
    right = high
    while left < right:
        while arr[left] <= pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], pivot

    return right

inp = [64, 34, 25, 12, 22, 11, 90] 

print('Input array = {}'.format(inp))

quick_sort(inp, 0, len(inp) - 1)

print('Sorted array = {}'.format(inp))
