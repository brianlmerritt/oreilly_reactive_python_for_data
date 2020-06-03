from rx import from_, operators as ops

source = from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.publish()
)

source.subscribe(lambda s: print("Subscriber 1: {0}".format(s)))
source.subscribe(lambda s: print("Subscriber 2: {0}".format(s)))

source.connect()
