import dictogram

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
    # NOTE: DERP don't need to look for words in the back of a sentence. That's not how English works lol
    # ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    iterate through each word while looking 4 ahead. lookahead arbitrary
    # walk_steps = number of words to look forward 
    # account for a start + end word aka START => TOKEN => WALK
    # NOTE: NESTED dictionary that keeps track of each forward words
    # nested dict format: {current word: {next_word = 1, next_next_word = 0,...}}
    # Put each word + transitions in individual dictionary?
    # weighted random selection
    walk_steps = 4
    tmp_dict = {}
    step_counter = 0
    total_steps = len(token_list)

    for index in range(len(token_list) - 1):
        while step_counter < (walk_steps + index):
            if token_list[index] not in tmp_dict:
                # TODO: Appending the word to dictionary of dictionary tmp_dict
                # tmp_dict[index] = 
            elif token_list[index] in tmp_dict:
                # Append the value in nested dictionary
            step_counter += 1
        step_counter = 0
            
                


    for word in token_list:
        if index in range(len(token_list) - walk_steps):
            print("hello")

        

# TODO: Once Markov chain populated pick word after word





# https://eli.thegreenplace.net/2018/elegant-python-code-for-a-markov-chain-text-generator/
    # walk_steps = 4 # Arbitrary number 4 for now. Looks at next 4 words after.
    # test_dict = {}
    
    # for i in range(len(token_list) - walk_steps):
    #     current_word = 
    #     test_dict[]

# if word in self:
#             self[word] += count
#         else:
#             self[word] = count
#             self.types += 1
#         self.tokens += count

#         # freq
#                 return self.get(word, 0)


# Don't know if this function is required yet
# def markov_chain_walk()