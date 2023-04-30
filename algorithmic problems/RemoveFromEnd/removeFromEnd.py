# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    # find how many nodes there
    nodes_count = 0
    current = head
    while current is not None:
        nodes_count += 1
        current = current.next
    
    tmp = head
    del_node_pos = nodes_count - k + 1
    if del_node_pos == 1:
        head = tmp.next
    else:
        curr = head
        current_pos = 1
        while curr is not None:
            if current_pos == del_node_pos-1:
                curr.next = curr.next.next
                break
            else:
                current_pos += 1
                curr = curr.next
    while head is not None:
        print(head.value)
        head = head.next
def makeLL(number):
    objs = []
    for i in range(number):
        o = LinkedList(value=i)
        objs.append(o)
    for i in range(number-1):
        objs[i].next = objs[i+1]
    return objs[0]

head = makeLL(10)
removeKthNodeFromEnd(head, 10)