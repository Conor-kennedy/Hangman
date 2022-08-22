import random
from more_itertools import locate
from nltk.corpus import words

def hangman():
    lives = 5
    #friend enters word to be guessed
    word_chosen = input('Enter a word: ').lower()

    if word_chosen in words.words() and word_chosen.isalpha():
        print("Valid Entry")
        print()
    else:
        print("Invalid Entry. Please try again.")
        print("-------------------------------------------------")
        print()
        hangman()

    #hiding the word
    result_word = len(word_chosen) * '-'
    result_word_list = list(result_word)
    guessed_letter_set = set()

    while lives > -1 : 

        if lives == 0:
            print()
            print("--- Game over. Better luck next time ---")
            print("--- The word was " + word_chosen  + " ---")
            print()
            break

        print()
        print("----------------------------------------------------------------")
        print()
        word_string = ''.join(result_word_list)
        print("What is the following word?  >>>   " + str(word_string))
        print("Number of lives left: " + str(lives))
    
        if len(guessed_letter_set) > 0 :
            print("Guessed letters so far: " + str(guessed_letter_set))

        guessed_letter = input('Guess a letter: ').lower()

        if guessed_letter in guessed_letter_set:
            print("You already tried this, no lives deducted")
            continue
        else:
            guessed_letter_set.add(guessed_letter)

        listt = []
        for i in word_chosen:
            listt.append(i)

        #getting indices of where there is match with entered input and character in predefined string
        indices = list(locate(listt, lambda x: x == guessed_letter))
        if len(indices) > 0 :
            print()
            print("Correct entry")
            print()
            #changing from '-' in hidden word to the new correctly guessed letter
            for index in indices:
                result_word_list[index] = guessed_letter
                #print(''.join(result_word_list))
                guessed = (''.join(result_word_list))
        else:
            lives -= 1
            print("Unlucky, this is not in the word")
            continue

        if guessed == word_chosen:
            print()
            print("***** Congrats, game completed ***** ")
            print()
            break

hangman()

    

    
