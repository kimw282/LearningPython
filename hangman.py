
import random
import urllib.request

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


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




def main():
    restart_game = "yes"
    
    print('''
==============================================================

*     *     *     *    *     *****   *     *     *     *    *
*     *    * *    **   *   **    *   **   **    * *    **   *
*     *    * *    * *  *  *          * * * *    * *    * *  *
*******   *****   *  * *  *    ****  *  *  *   *****   *  * *
*     *  *     *  *   **   **    **  *     *  *     *  *   **
*     *  *     *  *    *    ******   *     *  *     *  *    *

==============================================================

''')

    while restart_game != "no":
        random_word = random.choice(word_list)
        guessed_words = ""
        word = len(random_word)*"_ "
        i = 0
        guess_word = word.split()

        while i < 10:
            if word == " ".join(list(random_word)):
                print(f"\nYou win! The word is {random_word}.")
                break
            print(f"\n\n{word}")
            print(f"\nGuessed: {guessed_words}")
            # Prompts player to input their guess
            player_guess = str(input("\nInput guess: ")).lower()
            # If player's guess is the word
            if player_guess == random_word:
                print(f"\nYou win! The word is {random_word}.")
                break
            # If player enters character or word that has already been guessed
            elif player_guess in guessed_words:
                print("\nChoose something new!")
            # If player enters valid response (one alphabet)
            elif player_guess.isalpha():
                # If player's guess is in the word
                if player_guess in random_word:
                    # In order to ensure repeating characters
                    for num in range(len(random_word)):
                        if player_guess == random_word[num]:
                            guess_word[num] = player_guess
                            word = " ".join(guess_word)
                # If player's guess is not in the word
                else:
                    i += 1
                    # Prints hangman image
                    print(f"\n{player_guess} is not right!\n\n{hangman_pics[i]}.")
                guessed_words += player_guess + ", "
            # If player enters invalid response
            else:
                print("\nInvalid input")
        if i == 10:
            print(f"\n\nBoo! You Lost!\n Th word is {random_word}")
        restart_game = input("\n\nRestart Game? [y/n]\n")


if __name__ == "__main__":
    main()