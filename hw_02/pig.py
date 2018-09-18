""" when it is a vowel just add "ay" to end
    otherwise move first letter to end and add "ay" """
# Nursima Donuk and Shulamit Dashevsky
vowels = [ "a" , "e" , "i" , "o" , "u"]
def pig_latin(word):
    if word[0] in vowels:
    
        return word + "ay"
    else:
        return word [1:] + word[0] + "ay"
    
print (pig_latin('eat'))
print (pig_latin('hello'))
print (pig_latin('nursima'))

def pig_latin2(word):
    if word[0] == "a" or word[0] == "e" or word[0] =="i" or word[0] == "o" or word[0] == "u":
        return word + "ay"
    else:
        return word[1:] + word[0] + "ay"
print (pig_latin2('hello'))
print (pig_latin2('apple'))
print (pig_latin2('nursima'))

