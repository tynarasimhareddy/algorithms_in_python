
def find_max_sub_array(l1):
    res = temp_max = l1[0]
    for i in range(1, len(l1)):
        temp_max = max(temp_max + l1[i], l1[i])
        if temp_max > res:
            res = temp_max
    return res

l1 = [1, -3, 2, 1, -1]
res = find_max_sub_array(l1)
print('Max sub array SUM = {}'.format(res))
