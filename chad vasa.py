def word_to_pig_latin(word):
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return word + "way"
    else:
        for i, char in enumerate(word):
            if char in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"

def sentence_to_pig_latin(sentence):
    words = sentence.split()
    pig_latin_words = [word_to_pig_latin(word) for word in words]
    return " ".join(pig_latin_words)

# Input sentence
input_sentence = "it is nice weather today"

# Convert to Pig Latin
pig_latin_sentence = sentence_to_pig_latin(input_sentence)

# Print the result
print(pig_latin_sentence)