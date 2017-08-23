class WordList():

    words = list(set([line.rstrip('\n') for line in open('nynorsk.txt')]))
