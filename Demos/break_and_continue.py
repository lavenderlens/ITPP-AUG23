band = ["Bruce", "Patti", "Max", "Gary", "Soozie", "Stevie",
        "Nils", "Tom", "Clarence", "Jake", "Danny", "Roy"]

# keywords break and continue may be used in for and while loops that loop around a collection

for member in band:
    if member == "Stevie":
        break
    print(member)

for member in band:
    if member == "Stevie":
        continue
    print(member)

# works with while loops too but care to always increment counter
print('using while with break:')
counter = 0
while counter < len(band):
    if band[counter] == "Stevie":
        # because we break here we have no need to increment counter here
        break
    # after break is unreachable code
    else:
        print(band[counter])
        counter += 1

print('using while with continue:')
counter2 = 0
while counter2 < len(band):
    if band[counter2] == "Stevie":
        # because we CONTINUE here we MUST increment counter here AS WELL
        counter2 += 1
        continue
    # after break is unreachable code
    else:
        print(band[counter2])
        counter2 += 1
    # counter2 += 1 # doesn't work here
