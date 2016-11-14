def match(wordlist,letters):
    ''' assumes: wordList is a list of words in lowercase.
    lStr is a str of lowercase letters. No letter occurs in lStr
    more than once returns: a list of all the words in wordList that
    contain each of the letters in lStr exactly once and no letters not in lStr.'''
    match = []
    letters = sorted(letters)
    for i in wordlist:
        w=sorted(i)
        if w == letters:
            match.append(i)
    return match


wordlist = ['apple', 'boy', 'cat']
letters = 'tac'

print (match(wordlist,letters))



