from rx import from_

source = from_(["Alpha", "Beta", "Gamma"," Delta", "Epsilon"])

source.subscribe(lambda s: print("Subscriber 1: {0}".format(s)))
source.subscribe(lambda s: print("Subscriber 2: {0}".format(s)))
