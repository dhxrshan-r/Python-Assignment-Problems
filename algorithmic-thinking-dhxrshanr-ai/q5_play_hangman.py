""" Question 5: Hangman """
"""
Input: string
Output: interactive hangman game 
"""
def play_hangman(word):
    current_word="-"*len(word)
    guessed_letters=[]
    turns=0
    parts_left=6
    while parts_left!=0 and "-" in current_word:
        print("Current word:",current_word)
        print("Incorrect guesses left",parts_left)
        print("Letters guessed:",guessed_letters)
        user_guess=get_guessed_letters(guessed_letters)
        if user_guess in word:
            print("Good guess!!")
            current_word=update_current_word(user_guess,word,current_word)
        else:
            print("Not quite")
            parts_left-=1
        turns+=1
        guessed_letters.append(user_guess)
        print("-"*10 )
    print("Final word: ",current_word)
    if parts_left!=0:
        print("You won in",turns,"turns.")
    else:
        print("Game over @",turns,"Your chance has over")

def get_guessed_letters(guessed_letters):
    while True:
        letter=input("Which letter do you want to guess:")
        if len(letter)==1:
            if letter not in guessed_letters:
                return letter
            else:
                print("You already guessed that letter! Pick a different letter.")
        else:
            print("Please enter only one letter.")

def update_current_word(user_guess,word,current_word):
    new_current_word=""
    for ch in range(len(word)):
        if word[ch]==user_guess:
            new_current_word += user_guess
        else:
            new_current_word += current_word[ch]
    return new_current_word

"""
    for ch in range(len(word)):
        if user_guess == word[ch]:
            current_word = current_word[:ch]+user_guess+current_word[ch+1:]
    return current_word
"""

if __name__ == '__main__':
    play_hangman("program")

""" Sample Hangman game in Python terminal:

Current word: _ _ _ _ _ _ _ _ _ _ _ 
Incorrect guesses left: 6
Letters guessed: 
Which letter do you want to guess: e
Not quite...
-----
Current word: _ _ _ _ _ _ _ _ _ _ _ 
Incorrect guesses left: 5
Letters guessed: e
Which letter do you want to guess: o
Good guess!
-----
Current word: _ _ o _ _ _ _ _ _ _ _ 
Incorrect guesses left: 5
Letters guessed: e, o
Which letter do you want to guess: i
Good guess!
-----
Current word: _ _ o _ _ _ _ _ i _ _ 
Incorrect guesses left: 5
Letters guessed: e, o, i
Which letter do you want to guess: n
Good guess!
-----
Current word: _ _ o _ _ _ _ _ i n _ 
Incorrect guesses left: 5
Letters guessed: e, o, i, n
Which letter do you want to guess: g
Good guess!
-----
Current word: _ _ o g _ _ _ _ i n g 
Incorrect guesses left: 5
Letters guessed: e, o, i, n, g
Which letter do you want to guess: y
Not quite...
-----
Current word: _ _ o g _ _ _ _ i n g 
Incorrect guesses left: 4
Letters guessed: e, o, i, n, g, y
Which letter do you want to guess: as
Please enter only one letter.
Which letter do you want to guess: a
Good guess!
-----
Current word: _ _ o g _ a _ _ i n g 
Incorrect guesses left: 4
Letters guessed: e, o, i, n, g, y, a
Which letter do you want to guess: m
Good guess!
-----
Current word: _ _ o g _ a m m i n g 
Incorrect guesses left: 4
Letters guessed: e, o, i, n, g, y, a, m
Which letter do you want to guess: i
You already guessed that letter! Pick a different letter.
Which letter do you want to guess: t
Not quite...
-----
Current word: _ _ o g _ a m m i n g 
Incorrect guesses left: 3
Letters guessed: e, o, i, n, g, y, a, m, t
Which letter do you want to guess: r
Good guess!
-----
Current word: _ r o g r a m m i n g 
Incorrect guesses left: 3
Letters guessed: e, o, i, n, g, y, a, m, t, r
Which letter do you want to guess: p
Good guess!
-----
Final word: p r o g r a m m i n g 
You won in 11 turns.
"""