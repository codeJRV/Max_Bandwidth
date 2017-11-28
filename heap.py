class HeapBase:
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __lt__(self, other):
        return self._key < other._key

class HeapPQ():

    def __init__(self,k,v):
        self.elementList = []
        if(k != None and v!=None):
            self.elementList.append(HeapBase(k,v))


    def show(self):
        for e in self.elementList:
            print("Key: ", e._key,"Value: ", e._value)

    def add(self,key,value):
        self.elementList.append(HeapBase(key,value))
        self._bubbleup(len(self.elementList) - 1)

    def heapify(self):
        start = self._parent(len(self.elementList) - 1)
        for j in range(start, -1, -1):
            self._bubbledown(j)

    def _swap(self, i, j):
        temp = self.elementList[i]
        self.elementList[i] = self.elementList[j]
        self.elementList[j] = temp

        #self.elementList[i],self.elementList[j] = self.elementList[j], self.elementList[i]

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
                self._swap(j,max_child)
                self._bubbledown(max_child)

    def _bubbleup(self, j):
        if(j>0):
            parent = self._parent(j)
            if self.elementList[j] > self.elementList[parent]:
                # Swap J and max
                self._swap(j,parent)
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

class DijkstrasHeap(HeapPQ):
    class Locator(HeapPQ):
        __slots__ = '_index'

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j
            self._key   = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key


    def add(self, key, value):
        token = self.Locator(key, value, len(self.elementList))
        # print(len(self.elementList))
        #print("Token",token._index,token._key,token._value)
        self.elementList.append(token)
        self._bubbleup(len(self.elementList) - 1)
        return token

    def update(self, loc, newkey, newval):
        #loc._index = self.elementList[newval]
        j = loc._index

        #for e in self.elementList:
        #    print("element:", e._key,e._value,e._index)

        #print("Len" ,len(self.elementList))
        #print("Token", loc._index, loc._key, loc._value)

        loc._key = newkey
        loc._value = newval

        if j > 0 and self.elementList[j] > self.elementList[self._parent(j)]:
            self._bubbleup(j)
        else:
            self._bubbledown(j)

    def _swap(self, i, j):
        #print("Kidswap called")
        super()._swap(i,j)
        self.elementList[i]._index = j
        self.elementList[j]._index = i
        #print ("swapped:", self.elementList[i]._index, self.elementList[j]._index)





