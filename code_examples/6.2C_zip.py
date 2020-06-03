from rx import from_, zip, operators as ops

letters = from_(["A", "B", "C", "D", "E", "F"])
numbers = from_(range(1, 5))

# The code below includes l_n tuple unpacking (Python 3 doesn't support that out of the box, hence l_n[0] etc
zip(letters, numbers).subscribe(lambda l_n: print("{0}-{1}".format(l_n[0], l_n[1])))