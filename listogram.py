#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility

class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        self.list_of_list = []
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)
        # print("Corpus:"," ".join(word_list))
        print("self.list_of_list:",self.list_of_list)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        wordfound = False
        for token in self.list_of_list:
            if word == token[0]:
                wordfound = True
                token[1] += count
        if wordfound == False:
            self.list_of_list.append([word, count])
            # TOASK: Why didn't this work with += count?
            self.types += 1
        self.tokens += count  
         
        # wordfound = False   
        # for _list in self:
        #     if _list[0] == word and not wordfound:
        #         list_count = _list[1] + count
        #         self.append([word, list_count])
        #         wordfound = True
        #         self.tokens += count
        #     if not wordfound:
        #         self.append([word, count])
        #         self.tokens += count
        #         self.types += 1

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        wordfound = False
        for token in self.list_of_list:
            if word == token[0]:
                wordfound = True
                return token[1]
        if wordfound == False:
            return 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        wordfound = False
        for token in self.list_of_list:
            if word == token[0]:
                wordfound = True
                return True

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        
        wordfound = False
        for token in self.list_of_list:
            if target == token[0]:
                wordfound = True
            else:
                return None
        # if wordfound == False:
        #     self.list_of_list.append([word, count])

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()