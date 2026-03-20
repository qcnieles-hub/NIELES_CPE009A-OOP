def censor_sentence(sentence, bad_words):
    words = sentence.split()
    result = []

    for word in words:
        if word.lower() in bad_words:
            result.append("*" * len(word))
        else:
            result.append(word)

    return " ".join(result)



sentence = "This is a bad and ugly example"
bad_words = ["bad", "ugly"]

filtered_sentence = censor_sentence(sentence, bad_words)
print(filtered_sentence)