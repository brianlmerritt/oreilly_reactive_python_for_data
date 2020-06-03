from rx import create, from_callable

#  TODO fix this - Alpha is generated but followed by Completed

def MySubscriber(observer, scheduler):
    observer.on_next(next(iter(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])))
    observer.on_completed()

MyObserver = create(MySubscriber)

MyObserver.subscribe(
    on_next=lambda value: print(value),
    on_completed=lambda: print("Completed"),
    on_error=lambda error: print("Error occured: {0}".format(error))
)
