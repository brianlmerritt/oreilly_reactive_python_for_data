from rx import from_, operators as ops

from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.map(lambda s: len(s)),
    ops.distinct()
).subscribe(lambda i: print(i))
