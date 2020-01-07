# Longest common sub sequence
# with recursion
def lcs(x, y):
        if not x or not y:
                return ''
        if x[0] == y[0]:
                return x[0] + lcs(x[1:], y[1:])
        else:
                return max(lcs(x, y[1:]), lcs(x[1:], y), key=len)

print('LCS of {}, {} - {}'.format('thisis', 'estinglcs', lcs('thisis', 'estinglcs')))

# with dynamic programming
def lcs_dp(X, Y):
        table = [[0 for i in range(len(Y))] for j in range(len(X))]
        for i,x in enumerate(X):
                for j, y in enumerate(Y):
                        if x == y:
                                table[i][j] = table[i-1][j-1] + 1
                        else:
                                table[i][j] = max(table[i-1][j], table[i][j-1])

        result = ''
        x = len(X) - 1
        y = len(Y) - 1
        while x!=-1 and y!= -1:
                if x-1 != -1 and table[x][y] == table[x-1][y]:
                        x -= 1
                elif y-1 != -1 and table[x][y] == table[x][y-1]:
                        y -= 1
                else:
                        assert(X[x] == Y[y])
                        result = X[x] + result
                        x -= 1
                        y -= 1
        return result
print('LCS of {}, {} - {}'.format('thisis', 'estinglcs', lcs_dp('thisis', 'estinglcs')))
