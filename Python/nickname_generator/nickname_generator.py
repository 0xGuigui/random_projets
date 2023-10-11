import random


def shuffle_letters(words):
    all_letters = "".join(words)
    all_letters = list(all_letters)
    random.shuffle(all_letters)
    return "".join(all_letters)


def filter_by_length(shuffled_letters, min_length, max_length):
    filtered_letters = []
    for i in range(len(shuffled_letters) - (min_length - 1)):
        for j in range(min_length, max_length + 1):
            if i + j <= len(shuffled_letters):
                filtered_letters.append(shuffled_letters[i:i + j])
    return filtered_letters


def capitalize_first_letter(word):
    return word[0].upper() + word[1:]


input_words = input("Enter words separated by ', ': ").split(", ")
if input_words == [""]:
    print("No words entered")
    exit()

shuffled_letters = shuffle_letters(input_words)
if len(shuffled_letters) < 3:
    print("Not enough letters to generate a nickname")
    exit()

min_length = int(input("Enter minimum length of the word: "))
if min_length < 3:
    print("Minimum length must be at least 3")
    exit()

max_length = int(input("Enter maximum length of the word: "))
if max_length > len(shuffled_letters):
    print("Maximum length cannot be greater than the number of letters")
    exit()

number_of_words = int(input("Enter number of words to generate: "))
if number_of_words < 1:
    print("Number of words must be at least 1")
    exit()

filtered_letters = filter_by_length(shuffled_letters, min_length, max_length)
if len(filtered_letters) == 0:
    print("No words can be generated with the given constraints")
    exit()

for i in range(number_of_words - 1):
    print(capitalize_first_letter(random.choice(filtered_letters)), end=" " + '\n')
