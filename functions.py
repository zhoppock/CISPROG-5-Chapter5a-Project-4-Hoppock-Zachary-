import random

nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
articles = ("A", "THE")
prepositions = ("WITH", "BY")
adjectives = ("PRETTY", "RED", "HAPPY")

def sentence():
  option = random.randint(1, 2)
  if option == 1:
    return nounPhrase() + " " + verbPhrase()
  elif option == 2:
    return nounPhrase() + " " + verbPhrase() + " AND " + nounPhrase() + " " + verbPhrase()

def nounPhrase():
  option = random.randint(1, 2)
  if option == 1:
    return random.choice(articles) + " " + random.choice(nouns)
  elif option == 2:
    return random.choice(articles) + " " + random.choice(adjectives) + " " + random.choice(nouns)

def verbPhrase():
  option = random.randint(1, 2)
  if option == 1:
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()
  if option == 2:
    return random.choice(verbs) + " " + nounPhrase()

def prepositionalPhrase():
  return random.choice(prepositions) + " " + nounPhrase()
  
def main():
  number = int(input("Enter the number of sentences: "))
  for count in range(number):
    print(sentence())