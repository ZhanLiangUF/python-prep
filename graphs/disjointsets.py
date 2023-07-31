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