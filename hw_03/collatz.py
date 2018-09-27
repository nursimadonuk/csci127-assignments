#Nursima Donuk, Madison Chen, Crystal Fajardo 

def seq(n):
    count = 0
    while n != 1:
        print(n)
        if n % 2 == 0:        
            n = n // 2
        else:                 
            n = n * 3 + 1
        count += 1
    print(n) 
    return 'the while loop ran ' + str(count) +' times.'
    

print (seq(11))
print (seq(5))