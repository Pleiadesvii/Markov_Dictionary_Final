
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
        # if key1 in markov_dictionary:
        # else:
        #     print "try again!"
    return markov_dictionary
 
def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    random_key = random.choice(chains.keys())


    text_string = random_key[0] + " " + random_key[1]
    print text_string
    # make first key
    # add to string

    while random_key in chains: #setting end of loop
    #    list_of_values = markov_dictionary[key] #points to list of values for that key
    #     random_value = random.choice(list_of_values) # choose random value from list of values for that key
    #     text_string = text_string + str(key[0]) + " " + str(key[1]) + " " + random_value + " " # add to string
    #     key = (key[1], random_value)
    #     print text_string
        # else:
        #     return
    #print text_string
            

            # make new key (key2, value) = new_random_value

            #(key1, key2) : [1, 2, 3]
            #add key1, key2, random_value to string
            #then make a new key from (key2, random_value) : new_random_value


        
        
        
    
    #print text_string

    #return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

#input_text = "Some text"

# Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text

markov_dictionary = make_chains(file_object)
#print markov_dictionary
make_text(markov_dictionary)
