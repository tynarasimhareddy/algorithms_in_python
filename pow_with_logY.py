# Iterative approach with log(y)
# does not work for negative y values
def power(x, y):
    res = 1
    while y > 0:
        if (y & 1) == 1:
            res = res * x
        y = y >> 1
        x = x * x
    return res

#recursive method with log(y)
# this takes care of negative y values
def power2(x, y):
    if y == 0:
        return 1
    temp = pow(x, int(y/2))
    if y%2 == 0:
        return temp * temp
    else:
        if y > 0:
            return x * temp * temp
        else:
            return (temp * temp) / x


print(power(4, 2))
print(power2(4, -2))
print(power2(4, 2))
