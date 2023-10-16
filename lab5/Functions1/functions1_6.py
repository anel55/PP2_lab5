def reverse_word_order(sentence):
    words = sentence.split()
    words = list(reversed(words))
    return " ".join(words)

sentence = str(input())
print(reverse_word_order(sentence))
