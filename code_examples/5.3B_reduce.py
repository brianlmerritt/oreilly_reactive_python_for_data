from rx import from_, operators as ops

from_([4, 76, 22, 66, 881, 13, 35]).pipe(
    ops.filter(lambda i: i < 100),
    ops.reduce(lambda total, value: total + value)
).subscribe(lambda s: print(s))
