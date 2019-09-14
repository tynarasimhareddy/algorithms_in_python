
def gen_permutations(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            cur_val = lst[i]
            remaining_lst = lst[:i] + lst[i+1:]
            for p in gen_permutations(remaining_lst):
                l.append([cur_val]+p)
        return l

def gen_permutations_with_no_memory(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            cur_val = lst[i]
            remaining_lst = lst[:i] + lst[i+1:]
            for p in gen_permutations(remaining_lst):
                yield [cur_val]+p


text = list('abc')
for p in gen_permutations(text):
    print(''.join(p))


print('yield approach')
print('==============')
for p in gen_permutations_with_no_memory(text):
    print(''.join(p))

