from rx import from_, operators as ops

from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.filter(lambda s: len(s) >= 5),
    ops.take(2)
).subscribe(lambda s: print(s))
