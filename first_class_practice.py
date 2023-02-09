

# return a dictionary with count of each character in the string


def letter_count(text):
    char_dict = dict(zip([*text.lower()], [text.count(char) for char in text]))
    sorted_char_dict = dict(
        sorted(char_dict.items(), key=lambda x: (x[0], x[1])))
    return sorted_char_dict


letter = letter_count


def word_length(text):
    word_list = text.split(" ")
    counts = [len(word) for word in word_list]
    word_dict = dict(zip(word_list, counts))
    return word_dict


word = word_length

func_list = [letter, word]


def string_action(text, action):
    return action(text)


text = "My friend Sam bought me a large grapefruit"


print(string_action(text, func_list[0]))
print(string_action(text, func_list[1]))
