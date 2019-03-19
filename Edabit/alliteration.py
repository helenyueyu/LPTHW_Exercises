def alliteration_correct(sentence): 
  return len(set(w[0] for w in sentence.lower().split() if len(w) > 3)) == 1

print(alliteration_correct("She sells sea shells by the sea shore."))


