# Implements Lexicon class
import random

class Lexicon:
    def __init__(self, word_length):
        assert word_length > 0 and word_length < 44, "Invalid word length for Lexicon"

        self.word_length = word_length

        with open("dictionary.txt", "r") as file:
            reader = file.readlines()

            self.allwords = []
            self.words = []
            for line in reader:
                self.allwords.append(line.strip())

            for word in self.allwords:
                if len(word) == self.word_length:
                    self.words.append(word)


    def get_word(self):
        return random.choice(self.words)



# Implements Hangman class

class Hangman:

    def __init__(self, word, number_guesses):
        assert number_guesses <= 26, "Invalid number of guesses for Hangman"

        self.word = word
        self.number_guesses = number_guesses
        self.guesses = ""
        self.good_guesses = ""
        self.s = ""
        self.left_guesses = self.number_guesses - len(self.guesses)


    def is_valid_guess(self, letter):
        self.letter = letter
        if self.letter.isalpha() and len(letter) == 1:
            return True
        return False

    def guess(self, letter):
        assert len(letter) == 1 and letter.isalpha() and letter not in self.guesses, "Invalid letter for Hangman"

        self.letter = letter
        if self.letter not in self.guesses:
            self.guesses += self.letter

        if self.letter.lower() in self.word:
            self.good_guesses += self.letter.lower()
            return True
        return False

    def guesses_left(self):
        return self.number_guesses - len(self.guesses)

    def current_pattern(self):
        self.s = ""
        for letter in self.word:
            if letter in self.guesses:
                self.s = self.s +  letter
            else:
                self.s = self.s + "_"
        return self.s

    def is_running(self):
        if len(self.guesses) == self.number_guesses or self.s == self.word:
            return False
        return True

    def won(self):
        if self.s == self.word or len(self.guesses) == 26:
            return True
        return False



if __name__ == '__main__':

    print("WELCOME TO HANGMAN ツ")

    # prompt and re-prompt for word length
    word_length = int(input("What length of word would you like to play with?\n"))
    while word_length > 44 or word_length < 4:
        word_length = int(input("No words are longer than 44 letters!\n"))

    # load words
    lexicon = Lexicon(word_length)

    # prompt and re-prompt for number of guesses
    number_guesses = int(input("How many guesses are allowed?\n"))
    while number_guesses <= 0:
        number_guesses = int(input("Negative or zero guesses make no sense.\n"))

    # run an infinite number of games
    while True:

        # game set-up
        print(f"I have a word in my mind of {word_length} letters.")
        word = lexicon.get_word()
        game = Hangman(word, number_guesses)

        # allow guessing and provide guesses to the game
        while game.is_running():

            # prompt and re-prompt for single letter
            letter = input(f"Guess a letter ({game.guesses_left()} left): ")
            if len(letter) != 1 or not game.is_valid_guess(letter):
                continue

            # provide feedback
            if game.guess(letter):
                print("It's in the word! :))")
            else:
                print("That's not in the word :(")

            print(game.current_pattern())

        # after game ends, present the conclusion
        if game.won():
            print("Whoa, you won!!! Let's play again.")
        else:
            print(f"Sad, you lost ¯\_(ツ)_/¯. This was your word: {word}")
