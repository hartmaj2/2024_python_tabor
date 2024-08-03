import random
import os

def choose_word():
    words = ["python", "programming", "hangman", "summer", "camp", "detective", "secret", "agent"]
    return random.choice(words)

def display_hangman(tries):
    stages = ["""
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
                """,
                """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     /
                -
                """,
                """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |
                -
                """,
                """
                --------
                |      |
                |      O
                |     \\|/
                |
                |
                -
                """,
                """
                --------
                |      |
                |      O
                |     \\|
                |
                |
                -
                """,
                """
                --------
                |      |
                |      O
                |
                |
                |
                -
                """,
                """
                --------
                |      |
                |
                |
                |
                |
                -
                """
    ]
    return stages[tries]

def display_tried_words(tried_words):
    print("Tried words:",tried_words)

def display_tried_letters(tried_letters):
    print("Tried letters: ",tried_letters)

def play_hangman():
    word = choose_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    os.system("clear") # add here 
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        os.system("clear") # add here
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif guess.isalpha(): # remove unnecessary restriction
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        
        display_tried_letters(guessed_letters)
        display_tried_words(guessed_words)
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

if __name__ == "__main__":
    play_hangman()
