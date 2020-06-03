from rx import from_, operators as ops

items = ["134/34/235/132/77", "64/22/98/112/86/11", "66/08/34/778/22/12"]

from_(items).pipe(
    ops.flat_map(lambda s: from_(s.split("/"))),
    ops.map(lambda s: int(s))
).subscribe(lambda i: print(i))
