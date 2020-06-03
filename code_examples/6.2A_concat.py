from rx import from_, concat

source1 = from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])
source2 = from_(["Zeta", "Eta", "Theta", "Iota"])

concat(source1, source2).subscribe(lambda s: print(s))
