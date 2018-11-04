
def countApplesAndOranges(s,t,a,b,apples,oranges):
    new_apples = []
    new_oranges = []
    for positiona in apples:
        new_pa = a + positiona
        new_apples.append(new_pa)
    for positiono in oranges:
        new_po = b + positiono
        new_oranges.append(new_po)
    apple_count = 0
    orange_count = 0
    for itema in new_apples:
        if itema <= t and itema >= s:
            apple_count += 1
    for itemo in new_oranges:
        if itemo <= t and itemo >= s:
            orange_count += 1
    return apple_count, orange_count
    
        
print(countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4]))
print(countApplesAndOranges(4,8,10,2,[-3,-5,8],[5,2,-1]))





        
        