
# python 3.x
def insertion_sort(arr):
    for i in range(len(arr)):
        v = arr[i]
        j = i
        while(arr[j-1] > v and j>=1):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = v


input = [4,5,10,2,6,11]
print('Input array = {}'.format(input))
insertion_sort(input)
print('Sorted result = {}'.format(input))
