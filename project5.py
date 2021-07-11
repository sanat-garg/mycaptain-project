alphabets = {}
def addChar(al):
    isAlphaThere = (al in alphabets)
    if isAlphaThere == False:
        alphabets[al] = 1
    else:
        alphabets[al] += 1


word = input('\nEnter a word: ')
word = word.lower()
for x in word:
    addChar(x)

alphabets = str(alphabets)
alphabets = alphabets.replace("'","")
alphabets = alphabets.replace(":","=")
alphabets = alphabets[1:-1]
print('\nNumber of each alphabet the word contains are:\n'+alphabets + '\n')
