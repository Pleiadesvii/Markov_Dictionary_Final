
from sys import argv
# import random





class SimpleMarkovGenerator(object):

    def read_files(self):
        """Given a list of files, make chains from them"""
        file_names = argv[1:]
        raw_text = ""
        for name_of_file in file_names:  #looping over file names
            text_file = open(name_of_file) #for each file name, open the file name
            the_file = text_file.read() #read it
            raw_text += the_file #return it as a string
        self.raw_text = raw_text #stored raw_text in self

    def make_chains(self):
        """Takes input text as string; returns dictionary of markov chains."""
        markov_dictionary = {}
        listified_string = self.raw_text.split()
        for start_index in range(len(listified_string) - 2):
            key1 = listified_string[start_index]
            key2 = listified_string[start_index + 1]
            # line 20 replaces this line and appends values into the dictionary ->>> markov_dictionary[key1, key2] = word_list[start_index + 2]
            if (key1,key2) in markov_dictionary:
                markov_dictionary[(key1, key2)].append(listified_string[start_index+2])
            else: 
                markov_dictionary[(key1, key2)] = [listified_string[start_index+2]]
            # dictionary = [adding key_item1, key_item2] = adding value
        print markov_dictionary


test = SimpleMarkovGenerator()
test.read_files()

#test2 = SimpleMarkovGenerator()
test.make_chains()

    # def make_text(chains):
    #     """Takes dictionary of markov chains; returns random text."""

    #     random_key = random.choice(chains.keys())
    #     text_string = random_key[0] + " " + random_key[1]

    #     while random_key in chains: 
    #         list_of_values = chains[random_key] 
    #         random_value = random.choice(list_of_values) 
    #         text_string += " " + random_value + " " 
    #         random_key = (random_key[1], random_value)
            
    #     print text_string

# if __name__ == "__main__":
#     from sys import argv
#     corpus = argv[1]
#     file_object = open(corpus)
    


# markov_dictionary = make_chains(file_object)
# #print markov_dictionary
# make_text(markov_dictionary)
