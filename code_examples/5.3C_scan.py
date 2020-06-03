from rx import from_, operators as ops

from_([4,76,22,66,881,13,35]).pipe(
    ops.scan(lambda total, value: total + value)
).subscribe(lambda s: print(s))
