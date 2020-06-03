from rx import from_, operators as ops
from urllib.request import urlopen


def read_request(link):
    f = urlopen(link)

    return from_(f).pipe(
        ops.map(lambda s: s.decode("utf-8").strip())
    )

read_request("https://goo.gl/rIaDyM") \
    .subscribe(lambda s: print(s))
