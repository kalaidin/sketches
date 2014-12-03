sketches
========

aka Probabilistic data structures for mining in data streams, in pure Python.

Installation
------------
```
python setup.py install
```


HyperLogLog
-----------
Original paper: http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf

More on: http://research.neustar.biz/tag/hyperloglog/

Usage:
```
from sketches import HyperLogLog

h = HyperLogLog(10)

for i in range(100000):
  h.add(i)

print(h.estimate())

> 99860.5333365
```

Count-Min
-----------
Original paper: [here](https://7797b024-a-62cb3a1a-s-sites.googlegroups.com/site/countminsketch/cm-latin.pdf?attachauth=ANoY7cp6-21GfWiI_ZML2RI3KE6XBZkjF4IKIYot8slGRkcqklzZJMdxgEPo5gVJnEU5yQY2TQ4undOE7xdJMCWW_d0uHB6CUeNmukkGLZN8YB3aW7n_z4N17y5Av4Pr_rTg7EjLf6MUrULFANkSO19-fkaULT8bZy6iF1UIYZFXBdEpf7ojBmcpgwSnnSsY7bcSmMYFdLnhlhEjaC5JHpb-h9b_d5OBng%3D%3D&attredirects=0)

More on: https://sites.google.com/site/countminsketch/

Usage:
```
from sketches import CountMin

s = CountMin(10, 10)
data = np.random.zipf(2, 10000)
for v in data:
    s.add(v)

print(s.estimate(1))
> 6130.0

print(len([x for x in data if x == 1]))
> 6110
```

TODO:
----
- HLL improvements:
  - HLL++
  - Sliding window HLL
- Count-Mean-Min
- Stream-Summary
- Min-Hash
- Bloom filter
- Frugal sketches


