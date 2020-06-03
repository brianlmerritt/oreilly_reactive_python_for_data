from rx import interval, operators as ops
import time

disposable = interval(1).pipe(
    ops.map(lambda i: "{0} Mississippi".format(i))
).subscribe(lambda s: print(s))

# sleep 5 seconds so Observable can fire
time.sleep(5)

# disconnect the Subscriber
print("Unsubscribing!")
disposable.dispose()

# sleep a bit longer to prove no more emissions are coming
time.sleep(5)
