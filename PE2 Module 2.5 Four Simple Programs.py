import random

# Updated WORD_LIST with 15 words related to animals
WORD_LIST = ("ELEPHANT", "GIRAFFE", "KANGAROO", "DOLPHIN", "CROCODILE", 
             "ALLIGATOR", "CHEETAH", "LEOPARD", "PENGUIN", "OSTRICH", 
             "FLAMINGO", "HIPPOPOTAMUS", "RHINOCEROS", "CHIMPANZEE", "GORILLA")

def game(answer, display):
    wrong = 0
    right = 0
    max_wrong = 5

    print("Welcome to Code of Fortune")
    print("You will guess letters until you have the word")
    print(f"If you have {max_wrong} wrong guesses you will lose!")

    guessed_letters = []
    game_over = False

    while not game_over:
        for item in display:
            print(item, end=" ")

        print("\n\n")
        guess = input("Please enter a letter: ").upper()

        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
        else:
            guessed_letters.append(guess)
            bad_guess = True
            for i in range(len(answer)):
                if guess == answer[i]:
                    display[i] = guess
                    right += 1
                    bad_guess = False

            if bad_guess:
                print("Wrong!")
                wrong += 1
                print(f"Incorrect guesses left: {max_wrong - wrong}")

            if wrong >= max_wrong:
                print("You Lose!")
                print("The correct word was:", answer)
                game_over = True

            if right == len(answer):
                print("You Win!")
                print("The word was:", answer)
                game_over = True

def main():
    answer = random.choice(WORD_LIST)
    display = ["_"] * len(answer)
    game(answer, display)

main()
# This code implements a simple word guessing game where the player guesses letters
# to reveal a hidden word related to animals. The player has a limited number of wrong guesses