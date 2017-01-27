class Utils:

    @staticmethod
    def read_dictionary(path):
        words = []
        sorted_words = []
        dic_file = open(path)

        lines = dic_file.readlines()
        for line in lines:
            line = line.replace("\n", "")
            cols = line.split(",")
            words.append(cols[0])
            sorted_words.append(cols[1])
        return words, sorted_words

    @staticmethod
    def sort_word(word):
        return sorted(word)

    @staticmethod
    def count_wild_cards(tiles):
        return tiles.count(' ')

    @staticmethod
    def remove_wild_cards(tiles):
        return tiles.replace(" ", "")
