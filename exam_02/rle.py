"""def encode(s):
    new_l = []
    i = 0
 
    for letter in s:
        count = 1
        
        while i < len(s)-1:
            if s[i] == s[i+1]:
                count += 1
                i += 1
            else:
                count = count

            new_l.append([s[i],count])
            i += 1
  
    return new_l

print(encode("abbaaacddaaa"))"""





def encode(s):
    i = 0
    new_l = []
    while i < len(s)-1:
        count = 1
        if s[i] == s[i+1]:
            count += 1
            i+=1
        elif s[i] != s[i+1]:
            count = count
        new_l.append([s[i],count])
        i += 1
    return new_l
        
        
            
        
                     


print(encode("abbaaacddaaa"))
print(encode("abcd"))


def decode(l):
    str = ""
    for item in l:
        new_s = item[0] * item[1]
        str = str + new_s
    return str

print(decode([['a',1],['b',2],['a',3],['c',1],['d',2],['a',3]]))








































        
  
        
        
        