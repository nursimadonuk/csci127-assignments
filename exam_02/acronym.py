def makeacronym(w):
    w = w.lower()
    l = w.split()
    new_str = ""
    for word in l:
        new_str = new_str + word[0]
    return new_str

print(makeacronym("laugh out loud"))
print(makeacronym("Shaking my head"))
print(makeacronym("Read the... fine maual"))
print(makeacronym("In my humble opinion"))