from rx import interval, operators as ops


int1 = interval(2).pipe(
    ops.map(lambda i: "{0} Mississippi".format(i))
).subscribe(lambda s: print(s))

# Keep application alive until user presses a key
input("Press any key to quit")
