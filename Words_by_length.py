def arrange_words_by_length(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key=len)
    return ' '.join(sorted_words)


input_sentence = input("Enter a sentence: ")
output = arrange_words_by_length(input_sentence)
print("Output:", output)
