import random
words = ["python","program","computer","keywords","internet"]

word = random.choice(words)
guesses_letters = []
word_display = ["_"]*len(word)
max_attempts = 6
incorrect_guesses = 0

print("-------------HANGMAN GAME------------")
print("Guess the word , one letter at a time.")
print(f"You can make up to {max_attempts} incorrect guessess.\n")

while incorrect_guesses < max_attempts and "_" in word_display:
    print("Word:"," ".join(word_display))
    print("Guessed letters:",",".join(guesses_letters) if guesses_letters else "None")
    print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guesses_letters:
        print("You already guessed that letter. try another.\n")
        continue

    guesses_letters.append(guess)

    if guess in word:
        print("Good guess!\n")
        for i in range(len(word)):
            if word[i] == guess:
                word_display[i] = guess

    else:
        incorrect_guesses += 1
        print("Wrong guess!\n")


if "_" not in word_display:
    print("Word:"," ".join(word_display))
    print("Congratulations! You guesses the word!")


else :
    print("Game Over! You ran out of guesses.")
    print("The word was:", word)