
class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([char for char in word])

    def match(self, list):
        match_list = []

        for word in list:
            if sorted([char for char in word]) == self.word_letters:
                match_list.append(word)

        return match_list