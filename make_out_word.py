def make_out_word(out, word):
  firstpart, secondpart = out[:len(out)//2], out[len(out)//2:]
  return firstpart + word + secondpart
print (make_out_word('<<>>', 'yay'))