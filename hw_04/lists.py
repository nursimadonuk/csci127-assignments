#Nursima Donuk
import random

def build_random_list(size, max_value):
    """
    Parameters:
    size : the number of elements in the list
    max_value : the max random value to put in the list
    """
    
    l = []
    
    #make a loop that counts up to size
    
    i = 0
    while i < size:
        l.append(random.randrange(0, max_value))
        
        i += 1
    return l
print (build_random_list(10, 50))
        
        
def locate(l, value):
    if value in l:
        return l.index(value)
    else:
        return "-1"
    
print (locate([1,2,3,4,5,6,7,8,9,10], 7))

def count(l, value):
    i = 0
    count = 0
    while i < len (l):
        if l[i] == value:
            count += 1
        else:
            count = count
        i += 1
    return count
            
    #return l.count(value)  
print (count([1,8,3,8,5,6,7,8,8], 8))

def reverse(l):
    l_revs =[]
    i = 0
    ind = -1
    while i < len (l):
        l_revs.append(l[ind])
        i += 1
        ind -= 1
    return l_revs

print (reverse([1,2,3,4,5,6,7,8,9]))

def isIncreasing(l):
    i = 0
    count =0
    while i < len (l)-1:
        if l[i] < l[i+1]:
            count+=1
        else:
            return False
        i+= 1
    if count == len (l) -1:
        return True 
        
        
print (isIncreasing([1,2,1,4,5,6,7]))
print (isIncreasing([1,2,3,4,45,56,75,80]))
print (isIncreasing([5,9,11,54,78,10]))


def palindrome (l):
    i = 0
    a = -1
    count = 0
    if len(l) % 2 == 0:
        while i <= len(l)/2 :
            if l[i] == l[a]:
                count += 1
                i += 1
                a -= 1
            else:
                return False
            if count == len(l)/2:
                return True
    else:
        while i < len(l) // 2:
            if l[i] == l[a]:
                count += 1
                i += 1
                a -= 1
            else:
                return False
            if count == len(l)//2:
                return True
            
print (palindrome([1,2,3,4,4,3,2,1]))
print (palindrome([9,0,8,0,9]))
print (palindrome([1,2,3,4,5]))
print (palindrome([1,2,3,4]))
        
                
    
        
