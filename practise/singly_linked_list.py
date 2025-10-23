from typing import Any, Optional

class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional["Node"] = None

    def __repr__(self):
        return f"Node({self.data!r})"


class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.length: int = 0

    def append(self, value: Any) -> "SinglyLinkedList":
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            assert self.tail is not None  # for type-checkers
            self.tail.next = node
            self.tail = node
        self.length += 1
        return self

    def prepend(self, value: Any) -> "SinglyLinkedList":
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return self

    def remove(self, value: Any) -> Optional[Node]:
        """Remove first occurrence of value. Return the removed node or None."""
        if self.head is None:
            return None

        # If the head is the node to remove
        if self.head.data == value:
            removed = self.head
            self.head = self.head.next
            self.length -= 1
            if self.head is None:      # list became empty
                self.tail = None
            removed.next = None
            return removed

        prev = self.head
        current = self.head.next
        while current is not None:
            if current.data == value:
                prev.next = current.next
                if prev.next is None:   # removed last element
                    self.tail = prev
                self.length -= 1
                current.next = None
                return current
            prev = current
            current = current.next

        return None  # value not found

    def search(self, value: Any) -> Optional[Node]:
        current = self.head
        while current is not None:
            if current.data == value:
                return current
            current = current.next
        return None

    def print_list(self) -> None:
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        print(values)

    def __len__(self) -> int:
        return self.length

    def __repr__(self) -> str:
        vals = []
        cur = self.head
        while cur:
            vals.append(repr(cur.data))
            cur = cur.next
        return "SinglyLinkedList([" + ", ".join(vals) + "])"


#Example usage:
if __name__ == "__main__":
    lst = SinglyLinkedList()
    lst.append(10).append(20).append(30)
    lst.prepend(5)
    lst.print_list()          
    print(lst.search(20))     
    removed = lst.remove(20)
    print("removed:", removed) 
    lst.print_list()          
    print(len(lst))           
    print(lst)                
