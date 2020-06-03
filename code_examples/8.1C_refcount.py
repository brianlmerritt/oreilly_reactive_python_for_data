from rx import interval, operators as ops
import time

source = interval(1).pipe(
    ops.publish(),
    ops.ref_count()
)

source.subscribe(lambda s: print("Subscriber 1: {0}".format(s)))

# sleep 5 seconds, then add another subscriber
time.sleep(5)
source.subscribe(lambda s: print("Subscriber 2: {0}".format(s)))

input("Press any key to exit\n")