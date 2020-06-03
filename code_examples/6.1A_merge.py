from rx import from_, merge

source1 = from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])
source2 = from_(["Zeta", "Eta", "Theta", "Iota"])

merge(source1, source2).subscribe(lambda s: print(s))
