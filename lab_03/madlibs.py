#Nursima Donuk and William Lu

import random
sentence = 'Yesterday, <PERSON> and I went to the park. On our way to the <ADJECTIVE> park, <PERSON> and I saw a <ADJECTIVE> <NOUN> on a <NOUN> .'
PERSON = ['my professor', 'Sam', 'my friend', 'Alex', 'my dog', 'my mother']
ADJECTIVE =['pink', 'big', 'fast', 'gross', 'flat']
NOUN = ['bike', 'tank', 'toilet paper', 'cat', 'shoe']

def mad_libs(s):
    l = s.split()
    new_l = []
    person = (choose_random(PERSON))
    for item in l:
        if item == "<PERSON>":            
            new_l.append(person)
        elif item == "<ADJECTIVE>":
            new_l.append(choose_random(ADJECTIVE))
        elif item == "<NOUN>":                                                                        
            new_l.append(choose_random(NOUN))
        else:
            new_l.append(item)
    new_s = " ".join(new_l)
    return new_s

def choose_random(l):
    random_item = random.choice(l)
    return random_item
    
"""def random_noun():
    global Noun
    rndmn = random.choice(Noun)
    return rndmn

def random_person():
    global Person
    rndmp = random.choice(Person)
    return rndmp

def random_adj():
    global Adj
    rndma = random.choice(Adj)
    return rndma"""

for i in range(5):
    print(mad_libs(sentence))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    