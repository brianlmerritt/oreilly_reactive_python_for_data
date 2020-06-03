from rx import from_, concat

# Todo - find out why this is same as concat.  Look up concat_all if it still exists
source1 = from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])
source2 = from_(["Zeta", "Eta", "Theta", "Iota"])

concat(source1, source2).subscribe(lambda s: print(s))
