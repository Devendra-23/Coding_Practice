def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ""

print(longest_word("I love programming in Python"))  # programming