def spaces(numberOfSpaces):
    return (" " * numberOfSpaces)

def evaluateSequence(sequence):
    out = str(sequence[0])
    differences = spaces(len(str(sequence[0])))
    factors = spaces(len(str(sequence[0])))
    for idx, val in enumerate(sequence):
        if (idx > 0):
            # calculate difference and transform to string
            dif = val - sequence[idx-1]  # the difference between two values
            if (dif > 0):
                dif = "+" + str(dif)
            else:
                dif = str(dif)
            # calculate divisor and transform to string
            factor = "x" + ("%.5f" % (val / sequence[idx-1])).rstrip(".0") # the factor between the two values
            # calculat needed space for differences and factors
            neededSpaces = max(len(dif), len(factor))
            # append output strings
            differences += dif + spaces(neededSpaces-len(dif)) + spaces(len(str(sequence[idx])))
            factors += factor + spaces(neededSpaces-len(factor)) + spaces(len(str(sequence[idx])))
            out += spaces(neededSpaces) + str(val) # just the values
    return (out + "\n" + differences + "\n" + factors)

# get input
row = input("Enter a sequence of numbers (e.g. 6 18 21 63 66): ")
# transform to list
row = list(map(int, row.strip().split(" "))) # trim leading and ending spaces and separate by spaces

# detection for one "row"
print("\nTreated as single row:")
print(evaluateSequence(row))
print("\n")

# detection for two "rows"
print("Treated as two rows:")
firstRow = row[0::2]
print(evaluateSequence(firstRow))
secondRow = row[1::2]
print(evaluateSequence(secondRow))
