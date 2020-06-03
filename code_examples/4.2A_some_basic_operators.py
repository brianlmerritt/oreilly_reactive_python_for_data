from rx import of, operators as ops

test = of(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])\

obs = test.pipe(
    ops.map(lambda s: len(s)),
    ops.filter(lambda i: i >= 5))

obs.subscribe(lambda value: print(value))