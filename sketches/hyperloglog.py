from math import log
import unittest

from .hashing import sha1_32


def get_first_n_bits(v, n):
    return v >> (32 - n)


def get_left_most_position(v, n):
    i = 1
    while i <= n and not v & 0x80000000:
        i += 1
        v <<= 1
    return i


class HyperLogLog(object):

    def __init__(self, b, hash_function=sha1_32):
        self.b = b
        self._hash_function = hash_function
        assert b >= 4, "b >= 4 is expected"
        self.m = 2**b
        self.alpha = self._pick_alpha(self.m)
        self.registers = [0] * self.m

    def __add__(self, other):
        assert self.m == other.m, "dimensions mismatch"
        self.registers = [max(x) for x in zip(self.registers, other.registers)]
        return self

    def _pick_alpha(self, m):
        if m == 16:
            return 0.673
        if m == 32:
            return 0.697
        if m == 64:
            return 0.709
        else:
            return 0.7213 / (1 + 1.079 / m)

    def _linear_counting(self, v):
        return self.m * log(self.m / v)

    def _correct(self, e):
        if e < 2.5 * self.m:
            # small range corrections
            v = len([x for x in self.registers if x == 0])
            if v != 0:
                return self._linear_counting(v)
            else:
                return e
        elif e <= 1. / 30 * 2**32:  # no corrections
            return e
        else:
            # large range corrections
            return -2**32 * log(1 - e / 2**32)

    def add(self, v):
        h = self._hash_function(v)
        j = get_first_n_bits(h, self.b)
        self.registers[j] = max(self.registers[j],
                                get_left_most_position(h << self.b,
                                                       32 - self.b))

    def estimate(self):
        raw_estimate = self.alpha * \
            self.m**2 / sum([2**-v for v in self.registers])
        return self._correct(raw_estimate)

    def error(self):
        return 1.04 / self.m**0.5


class MyTest(unittest.TestCase):

    def check_error_bounds(self, h, s):
        estimate = h.estimate()
        error = h.error()
        true_value = len(s)
        self.assertLess(abs(estimate - true_value) / true_value, error)

    def test_hyperloglog(self):
        h = HyperLogLog(10)
        s = set()
        for i in range(100000):
            s.add(i)
            h.add(i)
        for i in range(50000):
            s.add(i)
            h.add(i)
        self.check_error_bounds(h, s)

    def test_union(self):
        h1 = HyperLogLog(10)
        h2 = HyperLogLog(10)
        s = set()
        for i in range(100000):
            s.add(i)
            h1.add(i)
        for i in range(50000, 100000):
            s.add(i)
            h2.add(i)
        h3 = h1 + h2
        self.check_error_bounds(h3, s)


if __name__ == "__main__":
    unittest.main()
