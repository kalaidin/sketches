import numpy as np
import unittest
from .hashing import sha1_32


class CountMin(object):

    def __init__(self, d, w):
        self.d = d
        self.w = w
        self.estimators = np.zeros((d, w))
        self.p = 2**31 - 1
        self.a = np.random.randint(0, self.p, size=self.d)
        self.b = np.random.randint(0, self.p, size=self.d)

    def hash(self, v, i):
        return ((self.a[i] * sha1_32(v) + self.b[i]) % self.p) % self.w

    def add(self, v):
        for i in range(self.d):
            self.estimators[i][self.hash(v, i)] += 1

    def estimate(self, v):
        return min([self.estimators[i][self.hash(v, i)]
                    for i in range(self.d)])


class MyTest(unittest.TestCase):

    def test_count_min(self):
        d, w = 10, 10
        s = CountMin(d, w)
        n = 10000
        data = np.random.zipf(2, n)
        for v in data:
            s.add(v)
        self.assertGreater(s.estimate(3), s.estimate(4))


if __name__ == "__main__":
    unittest.main()
