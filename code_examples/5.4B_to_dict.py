from rx import from_, operators as ops

from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.to_dict(lambda s: s[0])
).subscribe(lambda i: print(i))

from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.to_dict(lambda s: s[0], lambda s: len(s))
).subscribe(lambda i: print(i))
