from collections import defaultdict

class Node:
    def __init__(self):
        self.data = defaultdict(Node)
        self.eow = False
        self.num_childs = 0

    def build(self, words):
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        if len(word) == 0:
            return
        
        ch = word[0].lower()
        if ch in self.data:
            node = self.data[ch]
        else:
            node = Node()
            self.data[ch] = node
            self.num_childs += 1
            
        if 1 == len(word):
            node.eow = True
        else:
            node.add_word(word[1:])

    def print_all(self, root, parent=[], words=[], return_first=False):
        if root.eow:
            words.append(''.join(parent))
            if return_first:
                return words[0]
        if root.num_childs == 0:
            return
        for ch in root.data.keys():
            self.print_all(root.data[ch], parent+[ch], words, return_first)
            if return_first and len(words) == 1:
                return words[0]

    def auto_complete(self, pattern):
        if len(pattern) == 0:
            return self.print_all(self, [], [], True)
        if pattern[0] in self.data:
            return self.data[pattern[0]].auto_complete(pattern[1:])
        return ''
        

root = Node()
root.build(['hi', 'hello', 'google', 'Google', 'go'])
words = []

root.print_all(root, [], words)
print('{}'.format(words))

for pattern in ['h', 'hi', 'g', 'go', 'he', 'hand', 'goo']:
    res = root.auto_complete(pattern)
    print('Auto word of "{}" is "{}"'.format(pattern, pattern+res))
