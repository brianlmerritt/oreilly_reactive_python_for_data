from rx import from_, operators as ops

from_(["Alpha", "Theta", "Kappa", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.map(lambda s: len(s)),
    ops.distinct_until_changed()
).subscribe(lambda i: print(i))


from_(["Alpha", "Theta", "Kappa", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.distinct_until_changed(lambda s: len(s))
).subscribe(lambda i: print(i))
