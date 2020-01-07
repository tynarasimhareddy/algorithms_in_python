def wildcard_match(inp_str, ptrn):
        if len(ptrn) == 0:
                return len(inp_str) == 0
        if ptrn[0] == '?':
                return len(inp_str) > 0 and wildcard_match(inp_str[1:], ptrn[1:])
        if ptrn[0] == '*':
                return wildcard_match(inp_str, ptrn[1:]) or (len(inp_str) > 0 and wildcard_match(inp_str[1:], ptrn))
        return len(inp_str) > 0 and inp_str[0] == ptrn[0] and wildcard_match(inp_str[1:], ptrn[1:])


print('inp - {}, pattern {} = {}'.format('cc', 'c', wildcard_match("cc", "c"))) # False
print('inp - {}, pattern {} = {}'.format('cc', 'cc', wildcard_match("cc", "cc"))) # True
print('inp - {}, pattern {} = {}'.format('ccc', 'cc', wildcard_match("ccc", "cc"))) # False
print('inp - {}, pattern {} = {}'.format('cc', '*', wildcard_match("cc", "*"))) # True
print('inp - {}, pattern {} = {}'.format('cc', 'a*', wildcard_match("cc", "a*"))) # False
print('inp - {}, pattern {} = {}'.format('ab', '?*', wildcard_match("ab", "?*"))) # True
print('inp - {}, pattern {} = {}'.format('cca', 'c*a*b', wildcard_match("cca", "c*a*b"))) # False
