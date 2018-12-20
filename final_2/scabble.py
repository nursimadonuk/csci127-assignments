def canMakeWord(letters, word):
    d = {}
    for letter in letters:
        if letter not in d.keys():
            d[letter] = 1
        else:
            d[letter] = d[letter] + 1
        
    count = 0
    for letter in word:
        if letter in d.keys() and d[letter] > 0:
            count += 1
            d[letter] = d[letter] - 1
        else:
            count = count
    if count == len(word):
        return True
    else:
        return False
    

print(canMakeWord("ladilmy", "daily"))
print(canMakeWord("eerriin", "eerie"))
print(canMakeWord("orrpgma", "program"))
print(canMakeWord("orppgma", "program"))


def withWild(letters, word):
    d = {}
    for letter in letters:
        if letter not in d.keys():
            d[letter] = 1
        else:
            d[letter] = d[letter] + 1
        
    count = 0
    for letter in word:
        if letter in d.keys() and d[letter] > 0:
            count += 1
            d[letter] = d[letter] - 1
        else:
            count = count
    if count == len(word):
        return True
    elif count != len(word):
        if (len(word) - count) <= d['?']:
            return True
        else:
            return False
    
print(withWild('eerriin?', 'eerie'))
print(withWild('abcde??ab?', 'abbccdd'))
print(withWild('dily??', 'dailydaily'))
    
