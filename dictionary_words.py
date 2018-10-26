import random
import sys
import time

start_time = time.time()

def generate_sentence():
    sentence_storage = []
    words = open('/usr/share/dict/words', 'r')
    tmp_dictionary = []
    for line in words:
        tmp_dictionary.append(line.strip('\n'))
    for index in range(0, len(tmp_dictionary)):
        while len(sentence_storage) < int(sys.argv[1]):
            randomizer = random.randint(0, len(tmp_dictionary) - 1)
            sentence_storage.append(tmp_dictionary[randomizer])
    return " ".join(sentence_storage)

if __name__ == '__main__':
    print(generate_sentence())
    print("My program took " + str(time.time() - start_time) + " to run")
