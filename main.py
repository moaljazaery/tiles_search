from config import Config
from utils import Utils
import sys

res = []

tiles = sys.argv[1]

wildcards_count = Utils.count_wild_cards(tiles)
tiles = Utils.remove_wild_cards(tiles)
tiles = Utils.sort_word(tiles)
tiles_len = len(tiles)

words, sorted_words = Utils.read_dictionary(Config.preprocessed_dictionary_path)

# loop through the dictionary
for index in range(0, len(words)):

    sorted_word = sorted_words[index]
    word = words[index]
    word_len = len(word)

    matches = 0
    tile_index = 0
    i = 0
    remain_wild_card = wildcards_count

    # loop through the tiles of one dictionary word
    for i in range(0, word_len):
        # find first possible tile match
        while tile_index < tiles_len and sorted_word[i] > tiles[tile_index]:
            tile_index += 1

        if tile_index >= tiles_len:
            break

        # match
        if sorted_word[i] == tiles[tile_index]:
            matches += 1
            tile_index += 1
        # miss
        else:
            # use wild_card if possible
            if remain_wild_card > 0:
                remain_wild_card -= 1
                matches += 1
            else:
                break

    if (matches + remain_wild_card) == len(word):
        res.append(words[index])

print("Total Results : " + str(len(res)))
print(res)
