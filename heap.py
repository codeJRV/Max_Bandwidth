class HeapBase:
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __lt__(self, other):
        return self._key < other._key

class HeapPQ():

    def __init__(self):
        self.elementList = []

    def show(self):
        for e in self.elementList:
            print("Key: ", e._key,"Value: ", e._value)

    def add(self,key,value):
        self.elementList.append(HeapBase(key,value))
        self.heapify()

    def heapify(self):
        start = self._parent(len(self.elementList) - 1)
        for j in range(start, -1, -1):
            self._bubbledown(j)

    def _bubbledown(self, j):
        if self._leftPesent(j):
            left = self._left(j)
            max_child = left
            if self._rightPresent(j):
                right = self._right(j)
                if self.elementList[right] > self.elementList[left]:
                    max_child = right
            if self.elementList[max_child] > self.elementList[j]:
                #Swap J and max
                temp = self.elementList[j]
                self.elementList[j] = self.elementList[max_child]
                self.elementList[max_child] = temp
                self._bubbledown(max_child)

    def _bubbleup(self, j):
        if(j>0):
            parent = self._parent(j)
            if self.elementList[j] > self.elementList[parent]:
                # Swap J and max
                temp = self.elementList[j]
                self.elementList[j] = self.elementList[parent]
                self.elementList[parent] = temp
                self._bubbleup(parent)

    def _parent(self, i):
        p = (i - 1) // 2
        return p

    def _left(self, i):
        l = 2 * i + 1
        return l

    def _right(self, i):
        r = 2 * i + 2
        return r

    def _leftPesent(self, j):
        return self._left(j) < len(self.elementList)

    def _rightPresent(self, j):
        return self._right(j) < len(self.elementList)

    def get_largest(self):
        print("Max Key: ",self.elementList[0]._key,"Max Value: ", self.elementList[0]._value)
        return (self.elementList[0]._key,self.elementList[0]._value)

    def remove_largest(self):
        if not self.elementList:
            raise Empty('Priority queue is empty.')

        temp = self.elementList[0]
        self.elementList[0] = self.elementList[len(self.elementList)-1]
        self.elementList[len(self.elementList) - 1] = temp

        element = self.elementList.pop()
        self._bubbledown(0)
        return (element._key, element._value)