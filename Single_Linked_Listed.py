class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class SLL:
    def __init__(self):
        self.head = None


# a = SLL()
# print(a)


first = Node(2)
second = Node(3)
a = Node(10)
first.next = second
second.next = a

SLL1 = SLL()
SLL1.head = first



while SLL1.head != None:
    print(SLL1.head.key)
    SLL1.head = SLL1.head.next