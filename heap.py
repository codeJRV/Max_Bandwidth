class Node:
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __lt__(self, other):
        return self._key < other._key

class HeapPQ(Node):

    def __init__(self,k,v):
        super().__init__(k,v)
        self.nodeList = []
        #if(k != None and v!=None):
        #    self.nodeList.append(Node(k,v))


    def show(self):
        for e in self.nodeList:
            print("Key: ", e._key,"Value: ", e._value)

    def add(self,key,value):
        self.nodeList.append(Node(key,value))
        self._bubbleup(len(self.nodeList) - 1)

    def heapify(self):
        start = self._parent(len(self.nodeList) - 1)
        for j in range(start, -1, -1):
            self._bubbledown(j)

    def _swap(self, i, j):
        temp = self.nodeList[i]
        self.nodeList[i] = self.nodeList[j]
        self.nodeList[j] = temp

        #self.nodeList[i],self.nodeList[j] = self.nodeList[j], self.nodeList[i]

    def _bubbledown(self, j):
        if self._leftPesent(j):
            left = self._left(j)
            max_child = left
            if self._rightPresent(j):
                right = self._right(j)
                if self.nodeList[right] > self.nodeList[left]:
                    max_child = right
            if self.nodeList[max_child] > self.nodeList[j]:
                #Swap J and max
                self._swap(j,max_child)
                self._bubbledown(max_child)

    def _bubbleup(self, j):
        if(j>0):
            parent = self._parent(j)
            if self.nodeList[j] > self.nodeList[parent]:
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
        return self._left(j) < len(self.nodeList)

    def _rightPresent(self, j):
        return self._right(j) < len(self.nodeList)

    def get_largest(self):
        print("Max Key: ",self.nodeList[0]._key,"Max Value: ", self.nodeList[0]._value)
        return (self.nodeList[0]._key,self.nodeList[0]._value)

    def remove_largest(self):
        if not self.nodeList:
            raise Empty('Priority queue is empty.')

        temp = self.nodeList[0]
        self.nodeList[0] = self.nodeList[len(self.nodeList)-1]
        self.nodeList[len(self.nodeList) - 1] = temp

        element = self.nodeList.pop()
        self._bubbledown(0)
        return (element._key, element._value)

class DijkstrasHeap(HeapPQ):
    class Locator(HeapPQ):
        __slots__ = '_index', '_key', '_value'

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j
            #self._key   = k
            #self._value = v

        def __lt__(self, other):
            return self._key < other._key


    def add(self, key, value):
        token = self.Locator(key, value, len(self.nodeList))
        # print(len(self.nodeList))
        #print("Token",token._index,token._key,token._value)
        self.nodeList.append(token)
        self._bubbleup(len(self.nodeList) - 1)
        return token

    def update(self, loc, newkey, newval):
        #loc._index = self.nodeList[newval]
        j = loc._index

        #for e in self.nodeList:
        #    print("element:", e._key,e._value,e._index)

        #print("Len" ,len(self.nodeList))
        #print("Token", loc._index, loc._key, loc._value)

        loc._key = newkey
        loc._value = newval

        if j > 0 and self.nodeList[j] > self.nodeList[self._parent(j)]:
            self._bubbleup(j)
        else:
            self._bubbledown(j)

    def _swap(self, i, j):
        #print("Kidswap called")
        super()._swap(i,j)
        self.nodeList[i]._index = j
        self.nodeList[j]._index = i
        #print ("swapped:", self.nodeList[i]._index, self.nodeList[j]._index)





