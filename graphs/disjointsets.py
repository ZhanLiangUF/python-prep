class DisjointSet(object):

  def __init__(self, arr):
    self.arr = arr

  def isConnected(self, p, q):
    return self.arr[p] == self.arr[q]

  def connect(self, p, q):
    pid = self.arr[p]
    qid = self.arr[q]
    for i in range(len(self.arr)):
      if self.arr[i] == pid:
        self.arr[i] = qid

set = DisjointSet([0,1,2,3,4,5,6])
set.connect(0,1)
set.connect(1,2)
set.connect(0,4)
set.connect(3,5)
print(set.isConnected(2,4))
print(set.isConnected(3,0))

class QuickUnionDS(object):
  def __init__(self, n):
    self.parent = [-1 for i in range(n)]

 	 
  def find(self, p):
    r = p
    while self.parent[r] >= 0:
      r = self.parent[r]
    return r

  def isConnected(self, p, q):
    return self.find(p) == self.find(q)

  def connect(self, p, q):
    i = self.find(p)
    j = self.find(q)
    self.parent[i] = j

      
set2 = QuickUnionDS(6)
set2.connect(0,1)
set2.connect(1,2)
set2.connect(0,4)
set2.connect(3,5)
print(set2.isConnected(2,4))
print(set2.isConnected(3,0))

class WeightedQuickUnionDS(object):
    def __init__(self, n):
        self.parent = [-1 for i in range(n)]
        self.sizes = [1 for i in range(n)]

    def find(self, p):
        r = p
        while self.parent[r] >= 0:
            r = self.parent[r]
        return r

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def connect(self, p, q):
        i = self.find(p)
        j = self.find(q)
        
        iSize = self.sizes[i]
        jSize = self.sizes[j]

        if iSize == jSize:
            self.parent[i] = j
            self.sizes[i] += 1

        if iSize > jSize:
            self.parent[j] = i

        if jSize > iSize:
            self.parent[i] = j

set3 = WeightedQuickUnionDS(6)
set3.connect(0,1)
set3.connect(1,2)
set3.connect(0,4)
set3.connect(3,5)
print(set3.isConnected(2,4))
print(set3.isConnected(3,0))




