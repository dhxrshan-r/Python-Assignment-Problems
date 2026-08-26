def play_hangman(word):
    current_word = "_" * len(word)
    guessed_letters = [] 
    turns = 0
    parts_left = 6
    
    while parts_left != 0 and "_" in current_word:
        print("Current word: ", current_word)
        print("Parts left: ", parts_left)
        print("Guessed letters: ", guessed_letters)

        letter = guess_letter_input(guessed_letters)
        
        if letter in word:
            print("Good guess!")
            current_word = update_current_word(letter, word, current_word)
        else:
            print("Wrong guess.")
            parts_left -= 1
        turns += 1
        guessed_letters.append(letter)
        
    print("Final Word is: " + current_word)
    
    if parts_left != 0:
        print("You Won!")
    else:
        print("You Lost!")
    return

def guess_letter_input(already_guessed):
    while True:
        guess = input("Which letter do you want to guess: ")
        if len(guess) == 1 and guess:
            if guess not in already_guessed:
                return guess
            else:
                print("You already guessed that letter! Pick a different letter.")
        else:
            print("Enter exactly one letter.")

def update_current_word(letter, word, current_word):
    for i in range(len(word)):
        if word[i] == letter:
            current_word = current_word[:i] + letter + current_word[i+1:]
    return current_word
play_hangman("cmvijay")