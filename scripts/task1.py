class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge(self, other):
        p = self.head
        q = other.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head
        middle = self.get_middle(self.head)
        next_to_middle = middle.next
        middle.next = None
        left = LinkedList()
        left.head = self.head
        left.merge_sort()
        right = LinkedList()
        right.head = next_to_middle
        right.merge_sort()
        self.head = LinkedList.sorted_merge(left, right)

    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


# Приклад використання:
if __name__ == "__main__":
    llist = LinkedList()
    for value in [15, 10, 5, 20, 3, 2]:
        llist.insert_at_end(value)
    print("Оригінальний список:")
    llist.print_list()
    llist.reverse()
    print("\nРеверсований список:")
    llist.print_list()
    llist.merge_sort()
    print("\nВідсортований список:")
    llist.print_list()
    # Створюємо другий відсортований список
    llist2 = LinkedList()
    for value in [7, 8, 9]:
        llist2.insert_at_end(value)
    # Об'єднання списків
    merged_list = LinkedList()
    merged_list.head = llist.sorted_merge(llist2)
    print("\nОб'єднаний відсортований список:")
    merged_list.print_list()