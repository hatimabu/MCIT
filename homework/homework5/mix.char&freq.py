def char_frequency(s):
    freq = {}
    for char in s:
        if char != ' ':
            freq[char] = freq.get(char, 0) + 1
    return freq

# Test
print(char_frequency("hello world"))  # Output: {'h':1, 'e':1, 'l':3, 'o':2, 'w':1, 'r':1, 'd':1}
