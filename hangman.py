import random
import wordlists as wl


# word_list = [word_list_animals, word_list_places, word_list_misc]
word_list = [wl.word_list_animals, wl.word_list_misc]

'''
hangman_pics = ["\n\n", "\n\n\n\n\n\n=========", 
        "\n      |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 
'''
hangman_pics = ["\n\n", "\n\n\n\n\n\n=========", 
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 

# Hangman Ascii Art from : https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c


def main():
    restart_game = "yes"
    
    print('''
==============================================================

*     *     *     *    *     ****   *     *     *     *    *
*     *    * *    **   *   **   *   **   **    * *    **   *
*     *    * *    * *  *  *         * * * *    * *    * *  *
*******   *****   *  * *  *   ****  *  *  *   *****   *  * *
*     *  *     *  *   **   **   **  *     *  *     *  *   **
*     *  *     *  *    *    *****   *     *  *     *  *    *

==============================================================

''')

    while restart_game != "no" and restart_game != "n":
        stop_flag = False
        while not stop_flag:
            theme = input("\nChoose theme: Input number or press Enter for random\n 1) Animals and Bugs"
                          "\n 2) Miscellaneous Words\n\n")
            if theme in ["1", "2"]:
                random_word = random.choice(word_list[int(theme) - 1])
                stop_flag = True
            elif theme == "":
                random_word = random.choice(random.choice(word_list))
                stop_flag = True
            else:
                print("\nInvalid input")
        
        guessed_words = []
        word = len(random_word)*"_ "
        i = 0
        guess_word = word.split()

        while i < 8:
            if word == " ".join(list(random_word)):
                print(f"\nYou win! The word is {random_word}.")
                break
            print(f"\n\n{word}")
            print(f"\nGuessed: {', '.join(sorted(guessed_words))}")
            # Prompts player to input their guess
            player_guess = str(input("\nInput guess: ")).lower()
            # If player's guess is the word
            if player_guess == random_word.lower():
                print(f"\nYou win! The word is {random_word}.")
                break
            # If player enters character or word that has already been guessed
            elif player_guess in guessed_words:
                print("\nChoose something new!")
            # If player enters valid response (one alphabet)
            elif player_guess.isalpha():
                # If player's guess is in the word
                if player_guess in random_word.lower():
                    # In order to ensure repeating characters
                    for num in range(len(random_word)):
                        if player_guess == random_word[num].lower():
                            guess_word[num] = player_guess
                            word = " ".join(guess_word)
                # If player's guess is not in the word
                else:
                    i += 1
                    # Prints hangman image
                    print(f"\n{player_guess} is not right!\n\n{hangman_pics[i]}.")
                guessed_words.append(player_guess)
            # If player enters invalid response
            else:
                print("\nInvalid input")
        if i == 8:
            print(f"\n\nBoo! You Lost!\nThe word is {random_word}")
        restart_game = input("\n\nRestart Game? [y/n]\n").lower().strip()
    if restart_game == "no" or restart_game == "n":
        print("\nThanks for playing! (＾∀＾）ゞ\n")


if __name__ == "__main__":
    main()