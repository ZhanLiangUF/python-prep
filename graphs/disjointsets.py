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
    self.parent = []
    for i in range(n):
      self.parent[i] = -1
  
  def find(self, p):
    r = p
    while self.parent[r] >= 0:
      r = self.parent[r]
    return r

  def isConnected(self, p, q):
    return self.find(p) == self.find(q)


## don't use value of -1 for weighted