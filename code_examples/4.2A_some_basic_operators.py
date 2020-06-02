from rx import of, operators as op

test = of(["Alpha","Beta","Gamma","Delta","Epsilon"])\

obs = test.pipe(
    op.map(lambda s: len(s)),
    op.filter(lambda i: i >= 5))

obs.subscribe(lambda value: print(value))