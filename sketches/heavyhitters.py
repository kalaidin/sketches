from collections import Counter
from .countmin import CountMin


class CountMinHeavyHitters(object):

    def __init__(self, k, w, d):
        self.c = CountMin(w, d)
        self.heap = Counter()
        self.processed = 0
        self.k = k

    def add(self, v):
        self.processed += 1
        self.c.add(v)
        estimate = self.c.estimate(v)
        if estimate > self.k * self.processed:
            self.heap[v] = estimate
        for l in list(self.heap.keys()):
            if self.heap[l] < self.k * self.processed:
                del self.heap[l]

    def estimate(self):
        return self.heap.most_common()
