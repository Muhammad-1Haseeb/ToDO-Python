import random
from words import words

hangman_art = {
    0 : ("   ",
         "   ",
         "   "),
    1 : (" o ",
         "   ",
         "   "),
    2 : (" o ",
         " | ",
         "   "),
    3 : (" o ",
         "/| ",
         "   "),
    4 : (" o ",
         "/|\\",
         "   "),
    5 : (" o ",
         "/|\\",
         "/  "),
    6 : (" o ",
         "/|\\",
         "/ \\")
}

def display_man(wrong_guesses):
    print("*****************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*****************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("Answer: " + " ".join(answer))

def get_valid_letter(guessed_letter):
    """
        Loop until user
        enter single correct
        guess
    """

    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if not guess.isalpha():
            print("Please enter a letter (A-Z).")
            continue

        if guess in guessed_letter:
            print(f"You have already guessed this letter: {guess}")
            continue

        return guess

def play_game():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    max_wrong = len(hangman_art) - 1

    while True:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = get_valid_letter(guessed_letter)
        guessed_letter.add(guess)

        if guess in answer:
            print(f"Correct '{guess}' is in the word")
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            print(f"Wrong '{guess}' is not in the word")
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            return True

        if wrong_guesses >= max_wrong:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            return False


def main():
    is_running = True
    while is_running:
        play_game()

        play_again = input("Play Again? (y/n): ").lower().strip()
        if play_again != 'y':
            is_running = False
            print("Thanks for playing.")

        else:
            print("\n" * 5)

if __name__ == "__main__":
    main()