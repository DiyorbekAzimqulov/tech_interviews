from typing import Optional, List

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


def construct_linked_list_from_array(array: list[int]) -> List[Node]:
    """
    accepts list of integers and returns the Linked List
    """
    i = 0
    head = Node(array[i])
    cur = head
    for i in range(1, len(array)):
        node = Node(array[i])
        cur.next = node
        cur = cur.next
    return head


def print_ll(head: List[Node]) -> None:
    while head:
        print(head.val)
        head = head.next


def remove_duplicates(head: Optional[Node]) -> Node:
    """
    remove duplicates from an unsorted singly Linked List
    """
    if not head:
        return head
    hash_set = set()
    prev = head
    cur = head
    while cur:
        if cur.val in hash_set:
            cur = cur.next
            prev.next = cur
        else:
            hash_set.add(cur.val)
            prev = cur
            cur = cur.next
    return head

array = [1, 1, 2, 5, 2, 1]
linked_list = construct_linked_list_from_array(array)
head = remove_duplicates(linked_list)
print_ll(head)