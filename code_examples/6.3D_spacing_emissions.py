from rx import from_, zip, interval

letters = from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])
intervals = interval(1)

# The code below includes l_n tuple unpacking (Python 3 doesn't support that out of the box, hence l_i[0])
zip(letters, intervals).subscribe(lambda l_i: print(l_i[0]))

input("Press any key to quit\n")
