def get_prefix_table(sub_str):
        prefix_table = [0 for i in range(len(sub_str))]
        j = 0
        i = 1
        for i in range(1, len(sub_str)):
                while j > 0 and sub_str[i] != sub_str[j]:
                        j = prefix_table[j - 1]
                if sub_str[i] == sub_str[j]:
                        j += 1
                prefix_table[i] = j
        return prefix_table

def kmp(inp_str, sub_str):
        prefix_table = get_prefix_table(sub_str)
        j = 0
        for i in range(len(inp_str)):
                while j > 0 and inp_str[i] != sub_str[j]:
                        j = prefix_table[j - 1]
                if inp_str[i] == sub_str[j]:
                        j += 1
                if j == len(sub_str):
                        print('Found {} in {} at {} location'.format(sub_str, inp_str, i - j + 1))
                        return
        print('Not Found {} in {}'.format(sub_str, inp_str))


kmp('hellohi', 'lo')
kmp('hellohi', 'l')
kmp('hellohi', 'r')
kmp('bcabababca', 'ababc')
kmp('bcabababca', 'abab')
kmp('bcabababca', 'ababd')
