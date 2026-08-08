import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

### YOUR CODE STARTS FROM HERE ###

guessed_letters = []      # letters the player has already tried
wrong_guesses = 0         # how many body parts are on the gallows
max_wrong = 6             # head, body, left arm, right arm, left leg, right leg

body_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg"]

def show_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter == " ":
            display += "  "        # keep spaces for phrases like "credit card"
        elif letter in guessed_letters:
            display += letter + " "
        else:
            display += "* "
    return display.strip()

def word_is_solved(word, guessed_letters):
    for letter in word:
        if letter != " " and letter not in guessed_letters:
            return False
    return True

print("Welcome to Hangman!")
print(show_word(word, guessed_letters))

while wrong_guesses < max_wrong and not word_is_solved(word, guessed_letters):
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        wrong_guesses += 1
        print(f"Wrong! Added: {body_parts[wrong_guesses - 1]}")
        print(f"Gallows so far: {body_parts[:wrong_guesses]}")

    print(show_word(word, guessed_letters))

print()
if word_is_solved(word, guessed_letters):
    print(f"You won! The word was '{word}'.")
else:
    print(f"Game over! All six body parts are on the gallows. The word was '{word}'.")