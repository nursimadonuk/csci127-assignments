#Nursima Donuk and William Lu
import random

def random_l(min,max,size):
    l = []
    for i in range(size):
        l.append(random.randrange(min,max+1))
    return l

list = random_l(0,10,100)
print(list)

def max(l):
    current_largest = l[0]
    for item in l:
        if item > current_largest:
            current_largest = item
        else:
            pass
    i = 0
    for num in l:
        if num == current_largest:
            return i
        i += 1
        
print("An index of the largest number in the list is, " + str(max(list)))

def freq(l,value):
    i = 0
    f = 0
    while i < len(l):
        if l[i] == value:
            f += 1
        else:
            pass
        i += 1
    return f

print ("2 appears " + str(freq(list,2)) + " times in the list.")


def mode(l):
    current_mode = l[0]
    i = freq(l,current_mode)
    for num in l:
        if freq(l,num) > i:
            i = freq(l, num)
            current_mode = num
            
    print("the mode appears " + str(i) + " times in the list. The mode is:")
    return current_mode
        
        
print(mode(list))
        
                
        
        
        
        
        
        
        
        
        
    
    
    