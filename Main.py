import Words


def get_word_length():
    word_length = 0
    while word_length == 0:
        try:
            word_length = int(input('Kor mange bokstavar er det i ordet?\n'))
        except:
            print('Du må skrive inn eit tal. Prøv igjen.\n')
    return word_length


def get_if_letter_in_word(letter):
    answer = ''
    while answer == '':
        answer = input('\nInneheldt ordet bokstaven ' + letter +
                       '? Ja eller nei?\n')
        if (answer == 'Ja') or (answer == 'ja'):
            return True
        elif (answer == 'Nei') or (answer == 'nei'):
            return False
        else:
            answer = ''
            print('Du må skrive enten ja eller nei\n')


def get_letter_pos_list(letter, words):
    letter_pos_list = ''
    while letter_pos_list == '':
        try:
            while letter_pos_list == '':
                letter_pos_list = input(
                    'Skriv inn nummer på posisjonar i ordet der bokstaven ' +
                    letter + ' er med:\n').split()
                if len(letter_pos_list) == 0:
                    letter_pos_list = ''
                    print('Du må skrive inn minst 1 tal. Prøv igjen\n')
                for i in range(len(letter_pos_list)):
                    letter_pos_list[i] = int(letter_pos_list[i]) - 1
                if (min(letter_pos_list) < 0) or (
                   (max(letter_pos_list) + 1) > words.word_length):
                    letter_pos_list = ''
                    print('Tal må vere større enn null og mindre enn ordlengde.\n')
        except:
            letter_pos_list = ''
            print('Du må skrive inn tal. Prøv igjen.\n')
    return letter_pos_list


def loop(words):
    while True:
        letter = words.get_letter_to_guess()
        answer = get_if_letter_in_word(letter)
        if answer:
            letter_pos_list = get_letter_pos_list(letter, words)
            for element in letter_pos_list:
                words.set_words_with_letter_in_pos(letter, element)
            for i in range(words.word_length):
                if i not in letter_pos_list:
                    words.set_words_without_letter_in_pos(letter, i)
        else:
            words.set_words_without_letter(letter)
        if len(words.get_words()) == 1:
            print('\nOrdet er ' + words.get_words()[0])
            break
        elif len(words.get_words()) == 0:
            print('\nOrdet er ikkje i ordboka')
            break
        print(words.get_words())


def main():
    words = Words.Words()
    words.word_length = get_word_length()
    words.set_words_with_length(words.word_length)
    # print(words.get_words())
    loop(words)

    # for i in range(len(letters)):
        # print(letters[i] + ': ' + str(frequencies[i]).rjust(5))


if __name__ == '__main__':
    main()
