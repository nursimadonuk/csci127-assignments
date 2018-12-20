def countPlurals(line):
    lst = line.split()
    count = 0
    for word in lst:
        if word[-1] == 's':
            count += 1
        else: count = count
    return count
    
    
print(countPlurals("hello I like flowers and dogs"))

def notPossesive(line):
    lst = line.split()
    count = 0
    for word in lst:
        if word[-1] == 's':
            if word[-2] == "'":
                count = count
            else:
                count += 1
        else:
            count = count
    return count

print(notPossesive("cats monkeys dog's cat's monkey bunny horses"))