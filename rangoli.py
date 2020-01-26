def print_rangoli(size):
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z']
    res = []
    for i in range(0,size):
        row = chars[size-1:i:-1] + chars[i:size]
        row = '-'*2*i+ '-'.join(row) + '-'*2*i
        res.append(row)
    res = res[::-1] + res[1::]

    for obj in res:
        print obj

print_rangoli(5)
'''
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

'''
print_rangoli(7)
'''
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
--g-f-e-d-c-b-c-d-e-f-g--
----g-f-e-d-c-d-e-f-g----
------g-f-e-d-e-f-g------
--------g-f-e-f-g--------
----------g-f-g----------
------------g------------
'''
