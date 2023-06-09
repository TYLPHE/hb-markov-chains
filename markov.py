"""Generate Markov text from text files."""

from random import choice
import os
import sys

def open_and_read_file(file_path_1, file_path_2 = None):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path_1).read()
    if file_path_2 != None:
        contents += open(file_path_2).read()
    return contents


def make_chains(text_string, n_words):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    lst = text_string.split()

    for i in range(len(lst) - n_words):
        tuple_list = []
        for j in range(n_words):
            tuple_list += [lst[j + i]]

        value = chains.get(tuple(tuple_list), [])
        if len(value) != 0:
            value.append(lst[i + n_words])
        else: 
            chains[tuple(tuple_list)] = [lst[i + n_words]]

    
    # for key in sorted(chains):
    #     print(key, chains[key])
    return chains


def make_text(chains, n_words):
    """Return text from chains."""
    # for key in sorted(chains):
    #     print(key, chains[key])

    words = []
    lst = list(chains.keys())
    random_key = choice(lst)

    counter = 0
    
    while ord(random_key[0][0]) > 91 or ord(random_key[0][0]) < 65:
        random_key = choice(lst)


    for n in range(n_words):
        words.append(random_key[n])

    while chains.get(random_key):

        random_word = choice(chains[random_key]) 
        words.append(random_word)
        tuple_key = []

        for n in range(1, n_words):
            tuple_key += [random_key[n]]

        tuple_key += [random_word]
        random_key = tuple(tuple_key)


    return ' '.join(words)


input_path1 = sys.argv[1]
input_path2 = None
try:
    if os.path.isfile(sys.argv[2]):
        input_path2 = sys.argv[2]
        n_words = int(sys.argv[3])
    else: n_words = int(sys.argv[2])
except IndexError:
    n_words = 2

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path1, input_path2)

# Get a Markov chain
chains = make_chains(input_text, n_words)

# Produce random text
random_text = make_text(chains, n_words)

print(random_text)
