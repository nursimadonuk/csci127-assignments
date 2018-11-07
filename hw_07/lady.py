def happyLadybugs(b):
    happy =  False
    if sameColors(b):
        if atLeastOneEmptySpace(b):
            happy = True
        else:
            if isAdjacent(b):
                happy = True
    if happy:
        return "YES"
    else:
        return "NO"
    
    
def sameColors(str):
    same = False
    for color in str:
        dic = {'color': 0}
        if color in "ABCDEGHIJKLMNOPQRSTUVWXYZ":
            for char in str:
                if char == color:
                    dic['color'] += 1
            if dic['color'] >= 2:
                same = True
            else:
                same = False
                break
    return same
"""

def sameColor(str):
    lst = []
    dic = {}
    for char in str:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            lst.append(char)
    for color in lst:
        dic[color] = 0
    for i in str:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for color in str:
                dic[color] += 1
    for key in lst:
        if dic[key] > 
"""

            
def atLeastOneEmptySpace(str):
    empty = False
    count = 0
    for char in str:
        if char == "_":
            count += 1
        else:
            count = count
    if count > 0:
        empty = True
    else:
        empty = False
    return empty
               
def isAdjacent(str):
    adjacent = False
    i = 0
    while i < len(str):
        if i == len(str)-1:
            if str[i] == str[i-1]:
                adjecent = True
            else:
                adjacent = False
        elif str[i] == str[i+1] or str[i] == str[i-1]:
            adjacent = True
        else:
            adjacent = False
        i += 1
    return adjacent

print(happyLadybugs("YYBBGG"))
print(happyLadybugs("YBGYBG"))
print(happyLadybugs("Y_BGGBY"))
print(happyLadybugs("BYG_BG"))

