# from replit import clear as clr # Importing Clear function to clear the screen after each guess.
import random as rd
import hangman_words as wd
import hangman_art as art

hart_stages = art.stages
h_logo = art.logo #3
word = wd.word_list
chosen_word = rd.choice(word)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
print(h_logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # clr() # Clr module will clear the screen after every guess

#If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display :
      print(f"You have already guessed {guess}.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

#Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            #Printing the correct answer if the player loses
            print(f'Pssst, the solution is {chosen_word}.')

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

#Import the stages from hangman_art.py and make this error go away.
    print(hart_stages[lives])
