from rx import create

def push_numbers(observer, scheduler):
    observer.on_next(100)
    observer.on_next(300)
    observer.on_next(500)
    observer.on_completed()

create(push_numbers).subscribe(on_next = lambda i: print(i))
