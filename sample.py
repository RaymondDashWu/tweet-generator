def stochastic_sampling(words_dict):
    """Calculates total values of all words in dictionary, and then calculates 
    percentages to total 100%. 
    Ex: {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'Blue': 1, 'l': 1}
    one: 1/9
    fish: (1+4)/9
    two: (1+4+1)/9
    ..."""
    dict_value_totals = 0
    total_percentage = 0 

    for value in words_dict:
        dict_value_totals += words_dict[value]
    for value in words_dict:
        new_value = words_dict[value]/dict_value_totals
        total_percentage += new_value
        words_dict[value] = total_percentage
    random_picker = random.random()
    # Used to pick the value closest to random.random() above
    # Ex: if random.random() returned .1, "one" would be selected because it's closest at .11
    return min(words_dict, key=lambda y:abs(float(words_dict[y])-random_picker))

def markov_chain(token_list):
    # PSEUDO BRAINSTORM
    # ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    # Starts off with try, except to account for out of range error
    # walk_steps = number of words to look forward 
    # NOTE: DERP don't need to look for words in the back of a sentence. That's not how English works lol
    # account for a start + end word aka START => TOKEN => WALK
    # dictionary that keeps track of each word forward words
    # walking: {current word, next_word += 1, next_next_word += 0,...}
    # Put each word + transitions in individual dictionary?
    # ex: {}
    # Possible TODO: in future account for sets of words. Ex: next 4 words
# https://eli.thegreenplace.net/2018/elegant-python-code-for-a-markov-chain-text-generator/
    
    for 

def markov_chain_walk