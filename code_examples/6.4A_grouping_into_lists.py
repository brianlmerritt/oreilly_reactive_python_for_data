from rx import from_, of, from_iterable, operators as ops, create

items = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]


from_(items).pipe(
    ops.group_by(key_mapper=lambda s: len(s)),
    ops.flat_map(lambda grp: grp.pipe(ops.to_list()))  
).subscribe(lambda i: print(i))