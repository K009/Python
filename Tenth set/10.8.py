import random
class RandomQueue:

    def __init__(self):
    	self.items = []

    def __str__(self):
        return str(self.items)

    def insert(self, item):
        if self.is_full():
            raise ValueError("kolejka jest pelna")
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            raise ValueError("kolejka jest pusta")
        randomElement = random.choice(self.items)
        self.items.remove(randomElement)
        return self.items

    def is_empty(self):
    	return not self.items

    def is_full(self):
    	return False

    def clear(self):
    	del self.items[:]

kolejka = RandomQueue()
kolejka.insert(2)
kolejka.insert(3)
kolejka.insert(4)
print(kolejka.__str__())
kolejka.remove()
print(kolejka.__str__())
kolejka.clear()
print(kolejka.__str__())