def frequency(unique, filtered):
    """Finds out how often each unique word is used and putting them all in a dictionary"""
    words_dict = {}
    for unique in filtered:
        if unique in words_dict:
           words_dict[unique] += 1
        else:
            words_dict[unique] = 1
    return words_dict