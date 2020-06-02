from rx import range, just

# Using Observable.range()
letters = range(1,10)
letters.subscribe(lambda value: print(value))

# Using Observable.just()
greeting = just("Hello World!")
greeting.subscribe(lambda value: print(value))
