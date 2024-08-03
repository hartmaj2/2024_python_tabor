# Nasledujici kod ma nejake chyby

# TODO: program hned ze zacatku selze a hra kvuli tomu nejde hrat
# najdi pomoci debuggeru, kde je problem

# TODO: pokud spatne hadame slovo, tak nam to nevezme body 
# spravne by se melo vypsat: "zadaneslovo is not the word."

# TODO: obrazovka se nemaze mezi tahy os.system("clear") nebo os.system("cls")
# zamysli se, kam by se to nejlepe hodilo, at ta hra vypada hezky

# TODO: vypisovat, jaka slova a pismenka uz jsme zkouseli, pridat funkce, ktere to udelaji
# def display_guessed_words(...)
# def display_guessed_letters(...)

# TODO: pokud zadame jako pokus nejaky nesmysl, tak se program zasekne v nekonecne smycce
# najdi pomoci debuggeru, kde se to deje


import random

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

def play_hangman():
    word = choose_word()
    word_completion = "_" * len(word)
    guessed = False
    tried_letters = []
    tried_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries < 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in tried_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                tried_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                tried_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in tried_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                tried_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            while not guessed:
                pass
            print("Not a valid guess.")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

if __name__ == "__main__":
    play_hangman()
