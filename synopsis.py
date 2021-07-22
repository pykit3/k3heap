import k3heap

h = k3heap.RefHeap([5, 1, 4, 2, 3])

while h.size > 0:
    print(h.pop())
