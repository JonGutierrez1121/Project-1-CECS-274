from Interfaces import Set
from DLList import DLList
import numpy as np

class ChainedHashTable(Set):
    class Node() :
        def __init__(self, key, value) :
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList) :
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2**self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=np.object)
        for i in range(n):
            t[i] = self.dtype()
        return t


    def _hash(self, key : int) -> int :
        return self.z * hash(key) % (2**self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n
        
    def find(self, key: object) -> object :
        h = self._hash(key)
        for i in range(len(self.t[h])):
            if self.t[h][i].key == key:
                return self.t[h][i].value
        return None
        
    def add(self, key: object, value: object):
        if self.find(key) is not None:
            return False
        if self.n+1 > len(self.t):
            self.resize()
        hash_value = self._hash(key)
        self.t[hash_value].append(self.Node(key,value))
        self.n = self.n + 1
        return True


    def remove(self, key : int)  -> object:
        if self.find(key) is None:
            return None
        else:
            hash_value = self._hash(key)
            list = self.t[hash_value]
            temp = None
            for i in range(len(list)):
                if list[i].key == key:
                    self.n -= 1
                    temp = list.remove(i)
            if len(self.t) > 3*self.n:
                self.resize()
            return temp
    
    def resize(self):
        if self.n == 2**self.d:
            self.d += 1
        if 2**self.d >= 3*self.n:
            self.d -= 1
        temp = self.alloc_table(2**self.d)
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                current_ele = self.t[i].get(j)
                h = self._hash(current_ele.key)
                temp[h].append(current_ele)
        self.t = temp

    def __str__(self):
        s = "\n"
        for i in range(len(self.t)):
            s += str(i) + " : "
            for j in range(len(self.t[i])):
                k = self.t[i].get(j)  # jth node at ith list
                s += "(" + str(k.key) + ", " + str(k.value) + "); "

            s += "\n"
        return s

#if __name__ == "__main__":
    #table = ChainedHashTable()
    #print(table.remove(12))
    #print(table.find(2))
    #table.add(55, "first")
    #print(table)
