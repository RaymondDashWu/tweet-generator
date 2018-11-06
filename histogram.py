import re
import sys
import random

def read_sterilize_source(source_text):
    # with open(source_text) as file:
    #     source = file.read()


    # Filters out all punctuation and white space (line breaks + spaces) using regex and
    # substitutes with a space " ". Then splits into array
    # Updated for edge cases '. Now keeps words that use ' as part of word (I've, haven't, etc.)
    filtered = re.sub(r'\W*[^\'\w+\']', " ", source).split()
    return filtered
# REFACTOR TO ACCOUNT FOR SENTENCES. IMPORTANT FOR MARKOV CHAINS


def unique_words(filtered):
    # Updated to account for uppercase letters by lowering all of them
    unique = []
    for word in filtered.lower():
        if word not in unique:
            unique.append(word)
    return unique

def frequency(unique, filtered):
    # Dictionary method
    words_dict = {}
    for unique in filtered:
        if unique in words_dict:
           words_dict[unique] += 1
        else:
            words_dict[unique] = 1
    return words_dict


def frequency_list_of_list(unique, filtered):
    listoflists = []
    for entry in unique:
        counter = 0
        for index in filtered:
            if entry == index:
                counter += 1
        listoflists.append([entry, counter])
    return listoflists

def frequency_list_of_tuples(unique, filtered):
    listoftuples = []
    for entry in unique:
        counter = 0
        for index in filtered:
            if entry == index:
                counter += 1
        listoftuples.append((entry, counter))
    return listoftuples

def stochastic_sampling(filtered):
    pass


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
print(read_sterilize_source("text-corpus.txt"))
# print(unique_words(read_sterilize_source("text-corpus.txt")))
print(frequency(unique_words("text-corpus.txt"),read_sterilize_source("text-corpus.txt")))


# toki-pona-the-egg.txt
# print(frequency(unique_words("toki-pona-the-egg.txt"),read_sterilize_source("toki-pona-the-egg.txt")))
