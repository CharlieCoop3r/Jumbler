#For each line in dictionary
    #create sorted version of line
    #compare to sorted version of input word
    #if they are the same
        #print the original (unsorted) line

#List dictionary words that match an anagram
#2023-10-1 by Charlie Cooper

#DICT = "shortdict.txt"
DICT = "dict.txt"

#The find method takes a string as an input
#dict_file is then looped through and each line is stripped and compared to a normalized version of both the line and the string input
#The matching string within dict_file is then printed out

def find(anagram: str):
    """Print words in DICT that match anagram.
  
    >>> find("gamma")
    gamma
    magma
  
    >>> find("nosuchword")

    >>> find("MAGAM")
    gamma
    magma

    >>> find("KAWEA")
    awake
  
    """
    dict_file = open(DICT, 'r')
    for line in dict_file:
        word = line.strip()
        if normalize(word) == normalize(anagram):
          print(word)

#normalize takes a string as an input
#A list is created where the capitalized characters from the input will be stored
#wordList is then sorted and returned


def normalize(word: str) -> list[str]:
    """Returns a list of characters that is canonical for anagrams.
    
    >>> normalize("gamma") == normalize("magam")
    True
    
    >>> normalize("MAGAM") == normalize("gamma")
    True
    
    >>> normalize("KAWEA") == normalize("awake")
    True
    
    >>> normalize("KAWEA") == normalize("gamma")
    False
    """
    wordList = []
    word = word.upper()
    for letter in word:
        wordList+=letter
    wordList = sorted(wordList)
    return wordList
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Doctests complete!")
    
