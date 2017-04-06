import random
import string

WORDLIST_FILENAME = "e:\!STUDIES\EDX\MIT python\week3_probleset_3_2\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
       if char not in lettersGuessed:
          return False
    return True
            



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    for char in secretWord:
          if char not in lettersGuessed:
              result+='_ '
          else:
              result+=char
    return result
    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    result=''
    for char in string.ascii_lowercase:
       if char not in lettersGuessed:
          result+=char
    return result
    

def hangman(secretWord):
    n=8
    lettersGuessed=""    
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is "+str(len(secretWord))+" letters long")
    while n>0:
        print ("------------")
        print ("You have "+str(n)+" guesses left")
        print ("Available letters:" + getAvailableLetters(lettersGuessed))
        guess= input("Please guess a letter:")
        guessInLowerCase = guess.lower()
        if guessInLowerCase in lettersGuessed:
            print ("Oops! You've already guessed that letter:"+getGuessedWord(secretWord, lettersGuessed))
        elif guessInLowerCase not in secretWord:
            lettersGuessed+=guessInLowerCase
            print ("Oops! That letter is not in my word:"+getGuessedWord(secretWord, lettersGuessed))
            n-=1
        else:
            lettersGuessed+=guessInLowerCase
            print("Good guess:"+getGuessedWord(secretWord, lettersGuessed)   )
            if isWordGuessed(secretWord, lettersGuessed):
                  print("------------")
                  print("Congratulations, you won!")
                  break
    if n==0:      
       print("------------")
       print("Sorry, you ran out of guesses. The word was else. ")
       
       
    
