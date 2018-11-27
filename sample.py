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
    """Returns a data structure of word A followed by word B in a nested dictionary.
    Ex: ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'two', 'fish']
    {'one': {'fish': 1}, 'fish': {'two': 2, 'red': 1, 'blue': 1}, 'two': {'fish': 2}, 'red': {'fish': 1}, 'blue': {'fish': 1}}"""
    walk_steps = 1
    nest_dict = {}
    step_counter = 0
    total_steps = len(token_list)

    for i in range(total_steps - 1):
        # Not necessary walk steps. Tried to account for longer more accurate lookaheads but don't know how to implement
        while step_counter < (walk_steps):
            # returns a nested dictionary of word A which is followed by word B
            # {'one': {'fish': 1}
            if token_list[i] not in nest_dict:
                tmp_dict = {}
                tmp_dict[token_list[i+1]] = 1
                nest_dict[token_list[i]] = tmp_dict
            elif token_list[i] in nest_dict:
                # iterates through nested dictionary and adds to words in the nested dictionary
                # ex: fish': {'two': 1} => fish': {'two': 2}
                if token_list[i+1] in nest_dict[token_list[i]]:
                    nest_dict[token_list[i]][token_list[i + 1]] += 1
                else:
                    nest_dict[token_list[i]][token_list[i + 1]] = 1
            step_counter += 1
        step_counter = 0
        print(nest_dict)
            
def markov_chain_walk()

if __name__ == '__main__':
  markov_chain(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'two', 'fish'])             

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