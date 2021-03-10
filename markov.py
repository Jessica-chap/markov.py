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
    split_content = text_string.split()
    chains = {}
    
    for i in range(len(split_content) -1):
        
        if (split_content[i], split_content[i + 1]) in chains:
            if i < (len(split_content) -2): 
                chains[(split_content[i], split_content[i + 1])] += [split_content[i+2]]

        else:
            if i < (len(split_content) -2):
                chains[(split_content[i], split_content[i + 1])] = [split_content[i+2]]

        
    return chains


def make_text(chains):
    """Return text from chains."""

    # words = []

    # #something like
    # key_list = chains.keys()
    # random_key_choice = choice(list(key_list))
    # words = words.append(random_key_choice)
    # print(words)
    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    # Keep looping until we reach a value of None
    # (which would mean it was the end of our original text)
    # Note that for long texts (like a full book), this might mean
    # it would run for a very long time.

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])
 
    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
