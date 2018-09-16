def capitalize (name):
    name = 'nursima donuk'
    cap = name.title()
    return cap
print (capitalize('nursima donuk'))

def init (name):
    name = 'nursima donuk'
    my_name = name.title()
    f = my_name[0]
    l = my_name[8:]
    ok = f + ". " + l
    return ok
print (init('nursima donuk'))

def part_pig_latin (name):
    name = 'hello'
    g = name[0] + 'ay'
    h = name[1:]
    a = h + g
    return a
print (part_pig_latin('hello'))

def make_out_word(out, word):
  firstpart, secondpart = out[:len(out)//2], out[len(out)//2:]
  return firstpart + word + secondpart
print (make_out_word('<<>>', 'yay'))

def make_tags(tag, word):
  return '<' + tag + '>' + word + '</' + tag + '>'
print (make_tags('i', 'yay'))