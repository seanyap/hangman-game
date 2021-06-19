
def word_to_dict(word):
    """word_to_dict converts a string to a dictionary: key = letter,
    value = list of indexes where letter is found"""
    word_dict = {}
    for count,letter in enumerate(word):
        if letter in word_dict:
            word_dict[letter].append(count)
        else:
            word_dict[letter] = [count]
    return word_dict

def check_guess(letter, letters_pending, letters_found):
    """check_guess checks to see if user guess the correct letter"""

    # correct guess
    if letter in letters_pending:
        letter_index = letters_pending[letter].pop(0) # return first letter's index
        letters_found.add(letter_index)
        
        # check if list is empty
        if len(letters_pending[letter]) == 0:
            del letters_pending[letter]
        
        return True

    return False


def display_word_status(word_found):
    pass


def main():
    print("Welcome to Hangman Game!\n")
    word = input("Please enter a word: ")

    letters_pending = word_to_dict(word) # a dict with key: letter, value: list of indexes where letter is found
    letters_found = set() # a set with all letter indexes found by user

    tries = 6
    while tries > 0:
        print(f"You have {tries} tries!")
        letter = input("Guess a letter")

        if check_guess(letter, letters_pending, letters_found):
            print("You found a letter!")
        else: 
            print("Incorrect letter. Try again!")
            tries -= 1

        display_word_status(letters_found)

        # empty dict means we found all letters
        if not letters_pending:
            print("Congratulations, you won!")

    if tries == 0:
        print("You lost, better luck next time...")

if __name__ == "__main__":
    main()