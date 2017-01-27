# Tiles searching

The method:

    - pre-process the dictionary:
    (because multiple tiles searching will be done on the same dictionary, preprocessing the dictionary will help to reduce the complexity)
    first remove all the words of length greater than the maximum tiles length
    store a sorted tiles version of all the words

    - pre-process the query tiles (QT):
        1- count the wildcards "spaces" (wild_cards)
        2- Remove the wildcards and put them aside
        3- sort it 

    - Matching:
    foreach sorted-tiles-set (T) the pre-processed dictionary (D):
        // initialize Query tiles (QT) index
        QT_index=0
        matches=0
        remaining_wild_cards= wild_cards
        - foreach tile(t) in (T):
                //find first possible tile match of t in QT
                while QT_index < QT_len and t > QT[QT_index]:
                    QT_index += 1
                // QT is done : can't find further match just break for current T
                if QT_index >= QT_len:
                    break
                // t matches QT at index QT_index : increase the matches and move to next QT
                if QT[QT_index] == t:
                    matches += 1
                    QT_index += 1

                else: // no match for t which means {t < QT[QT_index]}
                    //use one wild card if possible, else break because T doesn't match result
                    remain_wild_card -= 1
                    matches += 1

        - if matches + remaining wild cards == length of the word
                add corresponding word to T in the result list



Analysis:

    N is the number of the words in the dictionary
    M is the number of the tiles in the query
    W is the average length of the dictionary's word

    for pre-processing the dictionary, we need to sort all the words which costs O(N (W log(W))),
    and we will duplicate the space to store the preprocessed words O(2N) space

    for the matching part, at max we will have M comparison for each word in the dictionary.
    The complexity is O(N M). In our case M is constant so the complicity is linear O(N)



Run the code:

    - define the new paths and the maximum tiles length in the config path 
    - Run the pre-processing command in the terminal:
        python3 dictionary_preprocessing.py

    - Run the matching command in the terminal by passing "seven_tiles" as parameter, Please use quotations:
        python3 main.py "seven_tiles"

       Notice :You can use spaces for wildcards in the previous command


