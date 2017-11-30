_left = lambda i: 2 * i + 1
_right = lambda i: 2 * i + 2
_parent = lambda i: (i - 1) // 2

class Node:
    class _Element:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

class HeapPQ(Node):

    def _has_left(self, j):
        return (_left(j) < len(self._data))

    def _has_right(self, j):
        return (_right(j) < len(self._data))

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def bubbleup(self, j):
        dad = _parent(j)
        if j > 0 and self._data[j] > self._data[dad]:
            self._swap(j, dad)
            self.bubbleup(dad)

    def bubbledown(self, j):
        if self._has_left(j):
            left = _left(j)
            max = left
            if self._has_right(j):
                right = _right(j)
                if self._data[right] > self._data[left]:
                    max = right
            if self._data[max] > self._data[j]:
                self._swap(j, max)
                self.bubbledown(max)

    def __init__(self, contents=()):
        self._data = [self._Element(k, v) for k, v in contents]
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        start = _parent(len(self) - 1)
        for j in range(start, -1, -1):
            self.bubbledown(j)

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.append(self._Element(key, value))
        self.bubbleup(len(self._data) - 1)

    def remove_largest(self):
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self.bubbledown(0)
        return (item._key, item._value)

class DijkstrasHeap(HeapPQ):
    class Indexer(HeapPQ._Element):
        __slots__ = '_index'

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    def _swap(self, i, j):
        # print("Kidswap called")
        super()._swap(i, j)
        self._data[i]._index = i
        self._data[j]._index = j

    def add(self, key, value):
        token = self.Indexer(key, value, len(self._data))
        self._data.append(token)
        self.bubbleup(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newval):
        j = loc._index
        loc._key = newkey
        loc._value = newval
        if j > 0 and self._data[j] > self._data[_parent(j)]:
            self.bubbleup(j)
        else:
            self.bubbledown(j)

#Adapted and streamlined from a max-heap python implementation online