import random

words = ['apple','tiger','pizza','planet','window','rocket','garden','python','java','html']

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]  
attempts = 8  # Number of allowed attempts

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # Reveal 
    else:
        print("That letter doesn't appear in the word.")
        attempts -= 1


#conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You won!")
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost!")