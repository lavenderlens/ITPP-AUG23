band = ["Bruce", "Patti", "Max", "Gary", "Soozie", "Stevie", "Nils", "Tom", "Clarence", "Jake", "Danny", "Roy"]

hornSection = ("Jake", "Kurt") # a tuple: tuples are immutable

band.append("Alan") # method of list: lists are NOT immutable

trombone = ("Alan", "Lindsay") # tuple - confusing, not same as method above

biggerHornSection = hornSection + trombone # you can join tuples

print(band)

print(biggerHornSection)

