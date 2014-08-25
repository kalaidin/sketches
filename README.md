sketches
========

aka Probabilistic data structures for mining in data streams, in pure Python.


HyperLogLog
-----------
Original paper: http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf

More on: http://research.neustar.biz/tag/hyperloglog/

Usage:
```
from hyperloglog import HyperLogLog

h = HyperLogLog(10)

for i in range(100000):
  h.add(i)

print(h.estimate())

> 99860.5333365
```


TODO:
----
- HLL improvements:
  - HLL++
  - Sliding window HLL
- Count-Min
- Count-Mean-Min
- Stream-Summary
- Min-Hash
- Bloom filter
- Frugal sketches


