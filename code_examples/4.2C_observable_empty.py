from rx import empty

empty() \
    .subscribe(on_next= lambda s: print(s),
               on_completed= lambda: print("Done!")
               )
