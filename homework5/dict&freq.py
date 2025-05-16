def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Test
print(word_frequency("the cat and the dog"))  # Output: {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
