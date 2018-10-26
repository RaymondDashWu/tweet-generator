def reverse_word(word):
    

def reverse_sentence(sentence):

if __name__ == '__main__':
    should_continue = True
    prompt = input("Would you like to reverse a sentence or word?")
    while should_continue == True:
        if prompt.lower() == "sentence":
            sentence_prompt = input("What sentence would you like to reverse?")
            return reverse_sentence(sentence_prompt)
        elif prompt.lower() == "word":
            word_prompt = input("What word would you like to reverse?")
            return reverse_word(word_prompt)
        else:
            should_continue = True
            return "Sorry, I didn't catch that. Would you like to reverse a sentence or word?"