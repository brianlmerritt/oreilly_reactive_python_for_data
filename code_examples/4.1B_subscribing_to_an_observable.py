from rx import create, from_callable

#  TODO fix this - Alpha is generated but followed by Completed

def MySubscriber(observer, scheduler):
    #observer.on_next(next(iter(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]))) # Produces first item Alpha then stops
    #observer.on_next(iter(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])) # Returns list iterator object, not items iterated
    #observer.on_next(lambda: for item in ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]: yield item) # Syntax error - can't use for here, with or without lambda
    observer.on_completed()

MyObserver = create(MySubscriber)

MyObserver.subscribe(
    on_next=lambda value: print(value),
    on_completed=lambda: print("Completed"),
    on_error=lambda error: print("Error occured: {0}".format(error))
)
