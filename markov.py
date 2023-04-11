"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()
    # print(contents)
    return contents


def make_chains(text_string):
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
    
    for i in range(len(lst) - 2):
        word1 = lst[i]
        word2 = lst[i + 1]
        value = chains.get((word1, word2), [])
        if len(value) != 0:
            value.append(lst[i + 2])
        else: 
            chains[(word1, word2)] = [lst[i + 2]]


    for key in sorted(chains):
        print(key, chains[key])
    # print(type(sorted(chains)))
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    lst = list(chains.keys())
    random_key = choice(lst)
    
    words.append(random_key[0])
    words.append(random_key[1])

    while chains.get(random_key):
        random_word = choice(chains[random_key]) 
        words.append(random_word)

        random_key = (random_key[1], random_word)

    # print(words)

    return ' '.join(words)


input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
