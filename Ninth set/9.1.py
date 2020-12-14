class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.tail
        if self.tail == self.head:
            self.tail = self.head = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -=1
        return node

    def merge(self, other):
        print(other)
        while other.head:
            self.insert_tail(other.head)
            other.remove_head()
        print(other.head)
        # Węzły z listy other są przepinane do listy self na jej koniec.
        # Po zakończeniu operacji lista other ma być pusta.

    def clear(self):
        temp = self.head
        if temp is None:
            print("\n Not possible to delete empty list")
        while temp:
            print(alist.head)
            self.remove_head()

alist = SingleList()
blist = SingleList()

alist.insert_head(Node(11))
alist.insert_head(Node(12))

blist.insert_head(Node(311))
blist.insert_head(Node(312))

alist.merge(blist)
print(alist.tail)