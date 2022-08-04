'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed apple
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'p', the list would be ['_', 'p', 'p', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''

   
    word = ''
    word_guessed =[]
    num_letter = len(set(word))
    num_lives =0
    list_letters =[]

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        print(f'The mystery word has {len(self.word)} characters')

        for i in range(len(self.word)):
            self.word_guessed.append('_') 
        
        print(f'{self.word_guessed}')
        


        # TODO 2: Initialize the attributes as indicated in the docstring - complete
        # TODO 2: Print two message upon initialization:
        # 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters) - complete
        # 2. {word_guessed}= complete
        pass

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # print("check letter")
        
        letter = letter.lower()

        # for letter in self.word :
        #     if letter in self.list_letters:
        #         self.list_letters = self.list_letters.replace('_', letter)
        #     else: 
        #         self.num_lives = self.num_lives - 1
        if letter in self.word:

            #appends letter to list of tried letters
            self.list_letters.append(letter)

            #replace _ with letter in word
            #iterate self.word and if letter == letter in current position, replace letter 
            #in word_guessed at the same position
            for i in range(len(self.word)):
                if letter == self.word[i]:
                    self.word_guessed[i]==self.word[i]


        elif letter not in self.word:
            self.num_lives -= 1
            self.num_letter -= 1
            self.list_letters.append(letter)
            print(self.list_letters)
            print(self.num_lives)
            self.ask_letter()





        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase-complete 
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A word can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        pass

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''

        letter = input("Please, enter just one character: \n")
    
        check = True
        
        while check:

            if len(letter) == 1: 
                if letter not in self.list_letters:
                    self.check_letter(letter)

                    check = False

                else:
                    print(f"{letter} was already tried")
                    letter = input("Please, enter just one character: \n")

            else:
                letter = input("Please, enter just one character: \n")




        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter - complete
        # TODO 1: Assign the letter to a variable called `letter` - complete
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character" - complete
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried" - complete
        # TODO 3: If the letter is valid, call the check_letter method - complete
        pass

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()

# for word in play_game.word_list:
    if game.word == game.word_guessed:
        if game.num_lives == 0:
             print("You have won")
        else:
             print(f'You ran out of lives. The word was{game.word}')
        



    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
   
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"

 
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# 


