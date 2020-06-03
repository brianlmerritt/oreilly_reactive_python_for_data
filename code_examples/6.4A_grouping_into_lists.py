from rx import from_, operators as ops, of

items = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]

from_(items).pipe(
    ops.group_by(lambda s: len(s)),
    ops.flat_map(lambda grp: grp.to_list())  # Todo grp.to_list() of a groupedobservable is not working - fix it
).subscribe(lambda i: print(i))
