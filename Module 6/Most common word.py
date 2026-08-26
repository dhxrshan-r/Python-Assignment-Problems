def most_common_word(words):
    most_word = []
    most_count = 0
    for word in words:
        if words.count(word) > most_count:
            most_word = [ word ]
            most_count = words.count(word)
        elif words.count(word) == most_count and word not in most_word:
            most_word.append(word)
    if len(most_word) == 0:
        return None
    elif len(most_word) == 1:
        return most_word[0]
    else:
        return most_word
print(most_common_word([ "hello", "hello", "hello", "what", "a", "nice", "day", "hello" ]))