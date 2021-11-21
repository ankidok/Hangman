from hangmanascii import hangmanascii, wordList
import random
from time import sleep
from os import system
from sys import exit


class Hangman:
    def __init__(self):
        self.wordAndHint = random.choice(wordList)
        self.word = self.wordAndHint[0]
        self.hint = self.wordAndHint[1]
        self.spaces = list()
        self.guess = ''
        self.guessedSpaces = ""
        self.guessesLeft = 8
        self.control1 = 0
        self.control2 = 0
        self.menu()

    def menu(self):
        for i in range(0, len(self.word)):
            self.spaces.append("_")

        print(self.spaces)
        print(self.word)
        sleep(1)
        while True:
            system("cls")
            self.control1 = len(self.word)
            self.control2 = len(self.word)
            self.guessedSpaces = ' '.join(self.spaces)
            while True:
                print(hangmanascii[-self.guessesLeft])
                print(f"{self.guessesLeft} tane hakkınız kaldı")
                print(self.guessedSpaces)
                print("\n"+self.hint+"\n")
                self.guess = input('\nTahminde bulunun: ').upper()
                if self.guess.isalpha():
                    self.guess = self.guess[0]
                    break
                else:
                    print("\nLütfen bir karakter girin...")
                    sleep(1)
                    system('cls')
                    continue
            for i in range(0, len(self.word)):
                if self.word[i] == self.guess:
                    self.spaces[i] = self.guess
                    self.control1 -= 1
                    continue
            else:
                if not (self.control1 < self.control2):
                    self.guessesLeft -= 1

            if self.spaces.count('_') == 0:
                system("cls")
                print(hangmanascii[-self.guessesLeft])
                self.guessedSpaces = ' '.join(self.spaces)
                print(self.guessedSpaces)
                print("\nKelimeyi buldunuz, tebrikler...")
                sleep(1)
                exit()
            elif self.guessesLeft == 0:
                system("cls")
                print(hangmanascii[-self.guessesLeft])
                self.guessedSpaces = ' '.join(self.spaces)
                print(self.guessedSpaces)
                print("\nİstiklal mahkemelerinin kararıyla asıldın...\nBundan 100 sene sonra üzerinden rant "
                      "yapılacak...")
                sleep(2)
                exit()
            sleep(0.5)


Hangman()
