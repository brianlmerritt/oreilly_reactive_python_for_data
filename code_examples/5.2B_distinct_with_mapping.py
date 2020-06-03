from rx import from_, operators as ops

from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.distinct(lambda s: len(s))
).subscribe(lambda i: print(i))
