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

h = HyperLogLog(14)
for i in range(100):
  h.add(i)

print(h.estimate())
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


