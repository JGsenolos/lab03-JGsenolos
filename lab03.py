# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Replace each `pass` with your code, and use `return` to send the answer
# back (not `print`).


def pig_latin(word):
    # TODO (Part 1): return the Pig Latin form of a single lowercase word.
    #   If it starts with a vowel (a, e, i, o, u): add "way" to the end.
    #   Otherwise: move the first letter to the end and add "ay".
    if word[0].lower() == "a" or word[0].lower() == "a" or word[0].lower() == "e" or word[0].lower() == "i" or word[0].lower() == "o" or word[0].lower() == "u":
        word += "way"
        
    else:
        word = word[1:] + word[0].lower() + "ay"
        
    word = word.capitalize()
    return word


def word_lengths(sentence):
    # TODO (Part 2): return a list with the length of each word in `sentence`
    #   (words are separated by spaces).

    words = sentence.split()

    lengths = []

    for word in words:
        lengths.append(len(word))
    
    return lengths


def reverse_words(sentence):
    # TODO (Part 3): return `sentence` with the order of its words reversed.
    #   e.g. "hello world" -> "world hello"
    words = sentence.split()
    reverse = words[::-1]

    return " ".join(reverse)


def letter_counts(text):
    # TODO (Part 4 - STRETCH, optional): return a dictionary mapping each letter
    #   to how many times it appears in `text`. Ignore case, and ignore anything
    #   that isn't a letter.
    counts = {}

    for i in text.lower():
        if i.isalpha():
            if i not in counts:
                counts[i] = 1 # First time seeing the letter
            else:
                counts[i] += 1 # Just adds 1 if it already exists

    return counts


def main():
    # Optional scratch space - use this to try your functions with sample values.
    print(pig_latin("banana"))                    # ananabay
    print(word_lengths("the quick brown fox"))    # [3, 5, 5, 3]
    print(reverse_words("the quick brown fox"))   # fox brown quick the
    print(letter_counts("hello"))                 # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    pass


if __name__ == "__main__":
    main()
