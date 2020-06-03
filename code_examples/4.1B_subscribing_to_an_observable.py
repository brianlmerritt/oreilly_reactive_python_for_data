from rx import create

def MySubscriber(observer, scheduler):
    observer.on_next("Alpha")
    observer.on_next("Beta")
    observer.on_next("Gamma")
    observer.on_next("Delta")
    observer.on_next("Epsilon")
    observer.on_completed()

MyObserver = create(MySubscriber)

MyObserver.subscribe(
    on_next=lambda value: print(value),
    on_completed=lambda: print("Completed"),
    on_error=lambda error: print("Error occured: {0}".format(error))
)
