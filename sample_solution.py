import sys
from random import choice


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    chains = {}

    words = corpus.split()

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

        # or we could say "chains.setdefault(key, []).append(value)"

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    key = choice(chains.keys()) #chooses a random key from a list of tuples, which chains.keys creates
    words = [key[0], key[1]] #turning the tuple into a list
    while key in chains:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text)
        #
        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

        word = choice(chains[key]) #find a random value from possible values for that tuple and name it word
        words.append(word) #append word to list of previous
        key = (key[1], word) #redefining key to be the last two words in the list

    return " ".join(words) #after add a space between every item in the list


input_path = sys.argv[1]
input_text = open(input_path).read()

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text