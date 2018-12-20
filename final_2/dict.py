def addline(d, line):
    lower_line = line.lower()
    list_line = lower_line.split()
    for word in list_line:
        first = word[0]
        if first not in d.keys():
            d[first] = word
        elif first in d.keys():
            values = [d[first] , word]
            val2 = " ".join(values)
            d[first] = val2

    return d

d = addline({}, "Shes got a smile it seems to me")
d = addline(d, "Reminds me of childhood memories")
d = addline(d, "Where everything")
d = addline(d, "Was as fresh as the bright blue sky")
d = addline(d, "Now and then when I see her face")
d = addline(d, "She takes me away to that special place")
print (d)


def spellcheck(d, word):
    lower_word = word.lower()
    first_letter = lower_word[0]
    if first_letter in d.keys():
        d[first_letter] = d[first_letter].split()
    if lower_word in d[first_letter]:
        return True
    else:
        return False
        
        
print(spellcheck(d, "Away"))
print(spellcheck(d, "Nursima"))