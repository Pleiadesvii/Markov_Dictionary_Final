
import re
import random
from sys import argv

corpus = argv[1]
file_object = open(corpus)



def make_chains(file_object):
    """Takes input text as string; returns dictionary of markov chains."""
    markov_dictionary = {}
    whole_file = file_object.read()
    word_list = re.split(" |\n", whole_file)
    for start_index in range(len(word_list) - 2):
        key1 = word_list[start_index]
        key2 = word_list[start_index + 1]
        # line 20 replaces this line and appends values into the dictionary ->>> markov_dictionary[key1, key2] = word_list[start_index + 2]
        if (key1,key2) in markov_dictionary:
            markov_dictionary[(key1, key2)].append(word_list[start_index+2])
        else: 
            markov_dictionary[(key1, key2)] = [word_list[start_index+2]]
        # dictionary = [adding key_item1, key_item2] = adding value
    return markov_dictionary
 
def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    random_key = random.choice(chains.keys())
    text_string = random_key[0] + " " + random_key[1]

    while random_key in chains: 
        list_of_values = chains[random_key] 
        random_value = random.choice(list_of_values) 
        text_string += " " + random_value + " " 
        random_key = (random_key[1], random_value)
        
    print text_string


markov_dictionary = make_chains(file_object)
#print markov_dictionary
make_text(markov_dictionary)
