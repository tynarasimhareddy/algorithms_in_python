def combinations(elems):
        level = ['']
        for i in range(len(elems)):
                nlist = []
                for item in level:
                        nlist.append(item + elems[i])
                level += nlist
        return level[1:]

print('Combinations of abc is - {}'.format(combinations('abc')))
print('Combinations of aba is - {}'.format(combinations('aba')))
