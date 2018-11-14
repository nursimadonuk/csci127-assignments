#Nursima Donuk and Darren Liang

def read(file):
    f = open(file)
    text = f.read()
    f.close()
    return text

def clean(text):
    text = read(text)
    for p in "?!.;,:-\"'“”":
        text = text.replace(p, "")
    word_list = text.split()
    word_list = [word.capitalize() for word in word_list]
    for word in word_list:
        if not word.replace("-", "").isalpha():
            word_list.remove(word)
    return word_list


def word_pairs(text):
    word_list = clean(text)
    d= {}
    for word in word_list:
        if word not in d.keys():
            d[word] = []
    count = 0
    while count < len(word_list)-1:
        word = word_list[count]
        if word_list[count+1] not in d[word]:
            d[word].append(word_list[count+1])
        count += 1
        
    return d
            

print(word_pairs("moby-small.txt"))

