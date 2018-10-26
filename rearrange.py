import sys
import random

def rearrange_words(sampler):
    word_storage = []
    for index in range(1, len(sys.argv)):
        unique_word = False
        while unique_word == False:
            randomizer = random.randint(1, len(sys.argv) - 1)
            if sys.argv[randomizer] not in word_storage:
                unique_word = True
                word_storage.append(sys.argv[randomizer])
            else:
                unique_word = False
    return " ".join(word_storage)

if __name__ == '__main__':
    print(rearrange_words(sys.argv[1:len(sys.argv)]))


# Method 2

# sentence_storage = []
# sentence = input("Enter a sentence to be randomized:")
# sentence_array = sentence.split(" ")

# for word in range(0,len(sentence_array)):
#     new_word = random.randint(0, len(sentence_array) - 1)
#     sentence_storage.append(sentence_array[word])
    
# print(sentence_storage)