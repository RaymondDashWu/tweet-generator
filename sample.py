from pprint import pprint
from histogram import pick_random_word
from histogram import read_sterilize_source
import random
from dictogram import Dictogram

# corpus = "one fish two fish red fish blue fish two fish".split()
corpus = read_sterilize_source("sarcasm.txt")


def stochastic_sample(words_dict):
    """Calculates total values of all words in dictionary, and then calculates 
    percentages to total 100%. 
    Ex: {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'Blue': 1, 'l': 1}
    one: 1/9
    fish: (1+4)/9
    two: (1+4+1)/9
    ..."""
    dict_value_totals = 0
    total_percentage = 0
    tmp_dict = {}

    for value in words_dict:
        dict_value_totals += words_dict[value]
    for value in words_dict:
        new_value = words_dict[value]/dict_value_totals
        total_percentage += new_value
        tmp_dict[value] = total_percentage
        random_picker = random.random()
    for value in tmp_dict:
        if tmp_dict[value] >= random_picker:
            return value

def markov_chain_nth_order(token_list, order = 4):
    """Returns a data structure of word A followed by word B in a nested dictionary.
    Ex: ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'two', 'fish']
    {'one': {'fish': 1}, 'fish': {'two': 2, 'red': 1, 'blue': 1}, 'two': {'fish': 2}, 'red': {'fish': 1}, 'blue': {'fish': 1}}"""
    walk_steps = 1
    nest_dict = {}
    step_counter = 0
    total_steps = len(token_list)

    for i in range(total_steps - order):
            # returns a nested dictionary of word A which is followed by word B
            # {'one': {'fish': 1}
        type_storage = tuple(token_list[i + index] for index in range(order))
        if type_storage not in nest_dict:
            nest_dict[type_storage] = Dictogram()
            # Commented out. This is literally becoming Dictogram() esp after referencing my prior code
            # for word in type_storage:
                # if word in type_storage:
                #     nest_dict[word] += 1
                # else:
                #     nest_dict[word] = 1
        nest_dict[type_storage].add_count(token_list[i + order])
        


        
            
            
            
    #         tmp_dict = {}
    #         tmp_dict[token_list[i+1]] = 1
    #         nest_dict[token_list[i]] = tmp_dict
    #     elif token_list[i] in nest_dict:
    #         # iterates through nested dictionary and adds to words in the nested dictionary
    #         # ex: fish': {'two': 1} => fish': {'two': 2}
    #         if token_list[i+1] in nest_dict[token_list[i]]:
    #             nest_dict[token_list[i]][token_list[i + 1]] += 1
    #         else:
    #             nest_dict[token_list[i]][token_list[i + 1]] = 1
    #     step_counter += 1
    # step_counter = 0
    return nest_dict

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
        while step_counter < walk_steps:
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
    return nest_dict
            
def markov_chain_walk(chain):
    start_word = 'one'
    total_words_picked = 0
    words_picked_list = [start_word]

    while total_words_picked < 10:
        # possible_current_words = chain[start_word]
            # given histogram, pick one word at random based on frequency
        # start_word = stochastic_sample(chain)
        start_word = random.choice(corpus)
        # print('current_word:', current_word)
        words_picked_list.append(start_word)
        total_words_picked += 1
    return words_picked_list

if __name__ == '__main__':
    # corpus = read_sterilize_source("sarcasm.txt")
    # 1: Get a list of tokens from a sentence or file
    # corpus = "one fish two fish red fish blue fish two fish".split()
    # words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'two', 'fish']

    # 2: Create the Markov chain structure from the list of tokens
    chain = markov_chain_nth_order(corpus)
    # pprint(chain)
    # print(type(chain))

    # 3: Walk the Markov chain to get a list of words in the generated sentence
    sentence_list = markov_chain_walk(chain)
    print('sentence_list:', sentence_list)

    # 4: Turn the list of words into a printable sentence
    # Execute 10x. Don't worry about how to find end of sentence
    # sentence = ...
    # print(sentence)


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