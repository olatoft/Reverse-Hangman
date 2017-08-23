import File_IO


class Words():

    def __init__(self):
        self.words = File_IO.WordList().words
        self.frequency_list = []
        self.word_length = 0
        self.alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                          'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']

    def get_words(self):
        return self.words

    def set_words_with_length(self, n):
        new_words = []
        for word in self.words:
            if len(word) == n:
                new_words.append(word)
        self.words = new_words

    def set_words_with_letter_in_pos(self, letter, pos):
        new_words = []
        for word in self.words:
            if word[pos] == letter:
                new_words.append(word)
        self.words = new_words

    def set_words_without_letter_in_pos(self, letter, pos):
        new_words = []
        for word in self.words:
            if word[pos] != letter:
                new_words.append(word)
        self.words = new_words

    def set_words_without_letter(self, letter):
        new_words = []
        for word in self.words:
            if letter not in word:
                new_words.append(word)
        self.words = new_words

    def get_frequency(self):
        frequency_list = [0 for i in range(len(self.alphabeth))]
        # frequency_percent_list = []
        for i in range(len(self.alphabeth)):
            for word in self.words:
                if self.alphabeth[i] in word:
                    frequency_list[i] += 1
        self.frequency_list = frequency_list
        deletion_list = []
        for i in range(len(self.alphabeth)):
            if self.frequency_list[i] == len(self.words):
                deletion_list.append(i)
        for element in reversed(deletion_list):
            del self.frequency_list[element]
            del self.alphabeth[element]

        # for frequency in frequency_list:
            # frequency_percent_list.append(
                # round((frequency / len(words)) * 100, 1))
        # return frequency_percent_list

    def get_letter_to_guess(self):
        self.get_frequency()
        return self.alphabeth.pop(self.frequency_list.index(max(self.frequency_list)))
