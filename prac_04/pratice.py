text = "This is a sentence"
words = text.split()
three_words = [word for word in words if len(word)>3]
print(three_words)