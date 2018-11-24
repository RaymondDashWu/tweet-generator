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