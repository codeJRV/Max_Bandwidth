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
#
# class DijkstrasHeap(HeapPQ):
#
#     def __init__(self):
#         super().__init__()
#         index = []
#
#     def add(self,key,value):
#         element = []
#         element.append(HeapBase(key,value))
#         element.append(len(self.elementList))
#         print(element[0]._key , element[0]._value,element[1] )
#         self.elementList.append(element)
#         self.heapify()
#         return element
#
#     def update(self, idx, key, value):
#         print(idx)
#
#         j = idx[1]
#         print(j)
#         print(len(self.elementList))
#         #print(self.elementList[j])
#
#         if not (0 <= j<= len(self.elementList) and self.elementList[j-1] is idx):
#             raise ValueError('Invalid locator')
#         idx[0]._key = key
#         idx[0]._value = value
#
#         if j > 0 and self.elementList[j] > self.elementList[self._parent(j)]:
#             self._bubbleup(j)
#         else:
#             self._bubbledown(j)
#
#     def show(self):
#         for e in self.elementList:
#             print("Key: ", e[0]._key,"Value: ", e[0]._value, "Index:" , e[1] )
#
#     def remove_largest(self):
#         if not self.elementList:
#             raise Empty('Priority queue is empty.')
#
#         temp = self.elementList[0]
#         self.elementList[0] = self.elementList[len(self.elementList)-1]
#         self.elementList[len(self.elementList) - 1] = temp
#
#         element = self.elementList.pop()
#         self._bubbledown(0)
#         return (element[0]._key, element[0]._value)


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
        #print("Token",token)
        self.elementList.append(token)
        self.heapify()
        return token

    def update(self, loc, newkey, newval):
        j = loc._index
        #print("Jay" , j)
        #print("Len" ,len(self.elementList))
        #print(self.elementList[j])
        #if not (0 <= j < len(self.elementList) and self.elementList[j] is loc):
        #    raise ValueError('Invalid locator')
        loc._key = newkey
        loc._value = newval

        if j > 0 and self.elementList[j-1] > self.elementList[self._parent(j-1)]:
            self._bubbleup(j)
        else:
            self._bubbledown(j)



