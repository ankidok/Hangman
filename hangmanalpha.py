from hangmanascii import hangmanascii, wordList
import random
from time import sleep
from os import system
from sys import exit


class Hangman:
    def __init__(self):
        self.words = wordList
        self.word = random.choice(self.words)
        self.spaces = list()
        self.hint = ''
        self.hintedSpaces = ""
        self.hintsLeft = 8
        self.control1 = len(self.word)
        self.control2 = len(self.word)
        self.menu()

    def menu(self):
        for i in range(0, len(self.word)):
            self.spaces.append("_")

        print(self.spaces)
        print(self.word)
        sleep(1)
        while True:
            system("cls")
            self.hintedSpaces = ' '.join(self.spaces)
            while True:
                print(hangmanascii[-self.hintsLeft])
                print(f"{self.hintsLeft} tane hakkınız kaldı")
                print(self.hintedSpaces)
                self.hint = input('\nTahminde bulunun: ').upper()
                if self.hint.isalpha():
                    self.hint = self.hint[0]
                    break
                else:
                    print("\nLütfen bir karakter girin...")
                    sleep(1)
                    system('cls')
                    continue
            for i in range(0, len(self.word)):
                if self.word[i] == self.hint:
                    self.spaces[i] = self.hint
                    self.control1 -= 1
                    continue
            else:
                if not (self.control1 < self.control2):
                    self.hintsLeft -= 1

            if self.spaces.count('_') == 0:
                system("cls")
                print(hangmanascii[-self.hintsLeft])
                self.hintedSpaces = ' '.join(self.spaces)
                print(self.hintedSpaces)
                print("Kelimeyi buldunuz, tebrikler...")
                sleep(1)
                exit()
            elif self.hintsLeft == 0:
                system("cls")
                print(hangmanascii[-self.hintsLeft])
                self.hintedSpaces = ' '.join(self.spaces)
                print(self.hintedSpaces)
                print("İstiklal mahkemelerinin kararıyla asıldın...\nBundan 100 sene sonra üzerinden rant yapılacak...")
                sleep(2)
                exit()
            sleep(0.5)


Hangman()
