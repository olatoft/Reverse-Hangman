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
    answer = input('\nInneheldt ordet bokstaven ' + letter + '? Ja eller nei?\n')
    if (answer == 'Ja' or answer == 'ja'):
        return True
    if (answer == 'Nei' or answer == 'nei'):
        return False


def get_letter_pos_list(letter):
    letter_pos_list = input(
        'Skriv inn nummer på posisjonar i ordet der bokstaven ' +
        letter + ' er med:\n').split()
    for i in range(len(letter_pos_list)):
        letter_pos_list[i] = int(letter_pos_list[i]) - 1
    return letter_pos_list


def loop(words):
    while True:
        letter = words.get_letter_to_guess()
        answer = get_if_letter_in_word(letter)
        if answer:
            letter_pos_list = get_letter_pos_list(letter)
            for element in letter_pos_list:
                words.set_words_with_letter_in_pos(letter, element)
            for i in range(words.word_length):
                if i not in letter_pos_list:
                    words.set_words_without_letter_in_pos(letter, i)
        else:
            words.set_words_without_letter(letter)
        if len(words.get_words()) == 1:
            break
        print(words.get_words())
    print('\nOrdet er ' + words.get_words()[0])


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
