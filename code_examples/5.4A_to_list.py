from rx import from_, operators as ops

from_(["Alpha","Beta","Gamma","Delta","Epsilon"]).pipe(
    ops.to_list()
).subscribe(lambda s: print(s))
