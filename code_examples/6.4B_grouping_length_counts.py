from rx import from_, operators as ops

items = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]

from_(items).pipe(
    ops.group_by(lambda s: len(s)),
    # Todo grp.to_list() of a groupedobservable is not working - fix it
    ops.flat_map(lambda grp: grp.count().map(lambda ct: (grp.key, ct))),
    ops.to_dict(lambda key_value: key_value[0], lambda key_value: key_value[1])
).subscribe(lambda i: print(i))
