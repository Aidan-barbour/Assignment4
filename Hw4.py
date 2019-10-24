class SortedPriorityQueue:
    # class allows creation of items for priority queues, with a key and value
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __le__(self, other):
            return self._key <= other._key

    # create a list to contain future items
    def __init__(self):
        self._data = []

    # returns the number of items in data list
    def __len__(self):
        return len(self._data)

    # determines if list is empty or not
    def is_empty(self):
        return len(self._data)  == 0

    # returns item with smallest key
    def min(self):
        if self.is_empty():
            return None
        n = (self._data[0]._key, self._data[0]._value)
        return n

    # adds values to the list
    def add(self, key, value):
        new = self._Item(key, value) # creates new item
        if self.is_empty(): # if the list is empty, it just adds the item
            self._data.append(new)
        else:
            # if the list is not empty, it uses insertion sort to put the item into the correct sorted position
            for i, item in enumerate(self._data):
                if new <= item:
                    self._data.insert(i, new)
                    break
                elif i == len(self)-1:
                    self._data.append(new)
                    break

    def remove_min(self):
        if self.is_empty(): #returns none if no items to remove
            return None
        # returns smallest item and deletes it from list
        item = (self._data[0]._key, self._data[0]._value)
        del self._data[0]
        return item

    # simple function to show the items in the list
    def show(self):
        for i, item in enumerate(self._data):
            print(item._key, item._value, end=", ")

# testing
def main():
    spq = SortedPriorityQueue()
    spq.is_empty()
    spq.add(5, 'hamburger')
    spq.add(0, 'lettuce')
    spq.add(3, 'cheese')
    spq.add(1, 'tortilla')
    spq.add(4, 'salsa')
    spq.add(2, 'beans')
    spq.is_empty()
    spq.show()
    print()
    print(spq.min())
    print(spq.remove_min())
    spq.add(7, "sour cream")
    spq.show()
    print()
    print(spq.min())

if __name__ == '__main__':
    main()