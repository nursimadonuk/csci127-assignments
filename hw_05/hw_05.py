def filterodd(l): #returns the odd numbers from the list
    new_l =[]
    i = 0
    while i < len(l):
        if l[i] % 2 != 0:
            new_l.append(l[i])
        else:
            new_l = new_l
        i += 1
    return new_l

print(filterodd([3,21,69,5,5,80,12,8,0,6,20,3,6,24,5,8,6,12]))
    
    
def mapsquare(l): #returns a new list where te items are squared
    new_l=[]
    i =0
    while i < len(l):
        squared = l[i] ** 2
        new_l.append(squared)
        i += 1
    return new_l

print(mapsquare([11,12,13,14,15]))
"""or"""
t = mapsquare([16,17,18,19,20])
print (t)
