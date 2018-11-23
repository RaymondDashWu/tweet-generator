import re
import sys
import random

def read_sterilize_source(source_text):
    """Filters out all punctuation and white space (line breaks + spaces) using regex and
    substitutes with a space " ". Then splits into array
    Updated for edge cases '. Now keeps words that use ' as part of word (I've, haven't, etc.)"""
    # with open(source_text) as file:
    #     source = file.read()
    filtered = re.sub(r'\W*[^\'\w+\']', " ", source).split()
    return filtered
# TODO: REFACTOR TO ACCOUNT FOR SENTENCES. IMPORTANT FOR MARKOV CHAINS


def unique_words(filtered):
    """Finds unique words. Intended to take in the words from read_sterilize_source results"""
    # Updated to account for uppercase letters by lowering all of them
    unique = []
    for word in filtered:
        if word not in unique:
            unique.append(word)
    return unique

def frequency(unique, filtered):
    """Finds out how often each unique word is used and putting them all in a dictionary"""
    words_dict = {}
    for unique in filtered:
        if unique in words_dict:
           words_dict[unique] += 1
        else:
            words_dict[unique] = 1
    return words_dict


def frequency_list_of_list(unique, filtered):
    """UNUSED. Only for class assignment. Finds out how often each unique word is used and putting them all in a list"""
    listoflists = []
    for entry in unique:
        counter = 0
        for index in filtered:
            if entry == index:
                counter += 1
        listoflists.append([entry, counter])
    return listoflists

def frequency_list_of_tuples(unique, filtered):
    """UNUSED. Only for class assignment. Finds out how often each unique word is used and putting them all in a tuple"""
    listoftuples = []
    for entry in unique:
        counter = 0
        for index in filtered:
            if entry == index:
                counter += 1
        listoftuples.append((entry, counter))
    return listoftuples

def pick_random_word(words_list):
    rand_index = random.randint(0, len(words_list) - 1)
    return words_list[rand_index]

def random_word_tester(words_list):
    total_random_picked = 0
    tmp_dict = {}
    while total_random_picked < 10000:
        rand_word = pick_random_word(words_list)
        if rand_word in tmp_dict:
            tmp_dict[rand_word] += 1
        else:
            tmp_dict[rand_word] = 1
        total_random_picked += 1
    return tmp_dict

def stochastic_sampling(words_dict):
    dict_value_totals = 0
    total_percentage = 0 

    for value in words_dict:
        dict_value_totals += words_dict[value]
    for value in words_dict:
        new_value = words_dict[value]/dict_value_totals
        total_percentage += new_value
        words_dict[value] = total_percentage
    random_picker = random.random()
    return min(words_dict, key=lambda y:abs(float(words_dict[y])-random_picker))

def multiple_stochastic_sampling(words_dict):
    # TODO: DOES NOT WORK. Needs to append total results to array. As is only picks 1 result
    total_random_picked = 0
    dict_value_totals = 0
    total_percentage = 0 

    while total_random_picked < 10000:
        for value in words_dict:
            dict_value_totals += words_dict[value]
        for value in words_dict:
            new_value = words_dict[value]/dict_value_totals
            total_percentage += new_value
            words_dict[value] = total_percentage
        random_picker = random.random()
        total_random_picked += 1
        return min(words_dict, key=lambda y:abs(float(words_dict[y])-random_picker))
    
    # dict_value_totals = []
    # for value in words_dict:
    #     dict_value_totals.append(words_dict[value])
    # number_total = 0
    # for number in dict_value_totals:
    #     number_total += number
    
    # total_random_picked = []
    # while len(total_random_picked) < 10000:
    #     random_picker = random.randint(0, number_total)
    #     for value in words_dict:
    #         if random_picker < words_dict[value]:
    #             total_random_picked.append(value)
    #         random_picker -= words_dict[value]

    # # TO-FIX: Is not random over a sample of 10,000. Sample below. Logic possibly wrong but code functions as intended.
    # # {'fish': 1447, 'two': 1688, 'red': 1896, 'Blue': 2121, 'l': 2343, 'one': 506}
    # tmp_dict = {}
    # for word in total_random_picked:
    #     if word in tmp_dict:
    #         tmp_dict[word] += 1
    #     else:
    #         tmp_dict[word] = 1
    # return tmp_dict

if __name__ == "__main__":
    with open("text-corpus.txt", "r") as file:
        source = file.read()
    # removes symbols, punctuation, etc. from source text and puts in array
    sterilized_source = read_sterilize_source(source)
    # retrieves uniques from above sterilized source
    sterilized_source_uniques = unique_words(sterilized_source)
    # counts the instances of uniques in sterilized source text
    sterilized_source_frequency = frequency(sterilized_source_uniques, sterilized_source)


    # corpus_length = sum(filtered.values())
    # destination = random.randint(0, corpus_length)


    # for word in histogram:
    #     destination = destination - histogram[word]
    #     if destination < 0:
    #         return word
    # return filtered[random.randint(0,len(filtered) - 1)]

# one fish two fish blue fish red fish
clean_txt_list = read_sterilize_source("text-corpus.txt")
print(clean_txt_list)
unique_words_list = unique_words(clean_txt_list)
print(unique_words_list)
# print(frequency(unique_words("text-corpus.txt"),read_sterilize_source("text-corpus.txt")))
freq = frequency(unique_words_list, clean_txt_list)
print(freq)

# print(multiple_stochastic_sampling(freq))
# print(random_word_tester(sterilized_source))

print(stochastic_sampling(freq))
print(multiple_stochastic_sampling(freq))


# toki-pona-the-egg.txt
# print(frequency(unique_words("toki-pona-the-egg.txt"),read_sterilize_source("toki-pona-the-egg.txt")))
