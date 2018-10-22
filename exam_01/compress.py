def compress_word(w):
    new_l = []
    vowels = ['a','e','i','u','o','A','E','I','U','O']
    i = 0
    if w[0] in vowels:
        new_l.append(w[0])
    for i in w:
        if i in vowels:
            new_l = new_l
        else:
            new_l.append(i)
            
    new_w = "".join(new_l)
            
    return new_w



print(compress_word('apple'))
print(compress_word('halloween'))
print(compress_word('Special'))
        
        
        
def sentence(line):
    l = line.split()
    new_l = []
    for word in l:
        new_w = compress_word(word)
        new_l.append(new_w)
    new_s = " ".join(new_l)
    return new_s


print(sentence('I like to eat apple pie'))
print(sentence('Who is there'))
        
        
        