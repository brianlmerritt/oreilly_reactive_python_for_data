from rx import from_, interval, operators as ops

source1 = interval(10).pipe(ops.map(lambda i: "Source 1: {0}".format(i)))
source2 = interval(5).pipe(ops.map(lambda i: "Source 2: {0}".format(i)))
source3 = interval(3).pipe(ops.map(lambda i: "Source 3: {0}".format(i)))

from_([source1, source2, source3]).pipe(
    ops.merge_all()
).subscribe(lambda s: print(s))

# keep application alive until user presses a key
input("Press any key to quit\n")
