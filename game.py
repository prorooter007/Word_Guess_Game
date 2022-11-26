import random as rm
print("Let's Play A Game!!!")
name = input("What is your name? ")
print("Good Luck ! ", name)
words = ['nagpur', 'ramdeobaba', 'college', 'minor', 'python', 'word', 'game', 'engineering', 'artificial', 'intelligence', 'machine', 'learning' , 'shreyash']
print(words)
word = rm.choice(words)
print("Guess the words from the above list")
guesses = ''
turns = 2
while turns > 0:
  for char in word:
    if char in guesses:
      print(char, end=" ")
    else:
      print("_", end=" ")
  print()
  guess = input("guess a word:")
  guesses += guess
  if guess not in word:
    turns -= 1
    print("Wrong")
    print("You have", + turns, 'more guesses')
    if turns == 0:
      print("You Lose, Better luck next time")
  if guess in word:
    print("\nYou Win")
    print("The word is: ", word)
    break
