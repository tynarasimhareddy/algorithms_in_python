#Longest Increasing Subsequence
def findLis(s):
    if not s:
        return 0
    res = [0 for i in range(len(s))]
    res[0] = 1
    for i in range(1,len(s)):
        maxval = 0
        for j in range(i):
            if s[i] > s[j]:
                maxval = max(maxval, res[j])
        res[i] = maxval + 1
    print s
    print res
    return max(res)

print findLis([9,3,5,6,5,2,8])
