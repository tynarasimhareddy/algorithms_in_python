def quick_sort(arr, low, high):
        if low < high:
                pivot = find_pivot(arr, low, high)
                quick_sort(arr, low, pivot - 1)
                quick_sort(arr, pivot+1, high)

def find_pivot(arr, start, end):
        pivot = arr[start]
        left = start + 1
        right = end
        while left <= right:
                while left <= right and arr[left] <= pivot:
                        left += 1
                while left <= right and arr[right] > pivot:
                        right -= 1
                if left < right:
                        arr[left], arr[right] = arr[right], arr[left]
        arr[start], arr[right] = arr[right], pivot
        return right

arr = [4, 7, 9, 3, 2, 6, 1]
print('Input = {}'.format(arr))
quick_sort(arr, 0, len(arr) - 1)
print('Sorted output = {}'.format(arr))

arr = [64, 34, 25, 12, 22, 11, 90]
print('Input = {}'.format(arr))
quick_sort(arr, 0, len(arr) - 1)
print('Sorted output = {}'.format(arr))
