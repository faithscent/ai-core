'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

class Hangman:
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
        

    def check_letter(self, letter) -> None:
        
        if letter in self.word:

            self.list_letters.append(letter)
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


    def ask_letter(self):

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


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()

    if game.word == game.word_guessed:
        if game.num_lives == 0:
             print("You have won")
        else:
             print(f'You ran out of lives. The word was{game.word}')
        
 
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# 


