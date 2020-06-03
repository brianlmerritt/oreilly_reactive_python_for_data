from rx import create, from_


def MySubscriber(observer, scheduler):
    observer.on_next(for x in ["Alpha", "Beta", "Gamma","Delta","Epsilon"]:
        yield x)
    observer.on_error("Error occured")
    observer.on_completed()

MyObserver = create(MySubscriber)

MyObserver.subscribe(
    on_next = lambda value: print(value),
    on_completed = lambda void: print("Completed"),
    on_error = lambda error: print("Error occured: {0}".format(error))
)
