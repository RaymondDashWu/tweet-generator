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