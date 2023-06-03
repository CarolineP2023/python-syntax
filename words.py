# print("hello".upper())


def print_upper_words (words):
    """ prints each word on a seperate line, but in all uppercase 

            ie. print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
                    HELLO
                    HEY
                    GOODBYE
                    YO
                    YES
    """

    for word in words:
        print(word.upper())

def print_upper_words_letter (words):
    """ prints each word on seperate line that starts with the letter e, but in all uppercase

        ie. print_upper_words_letter(["everyone", "is", "Early"])
                    EVERYONE
                    EARLY
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words_start(words, starts_with):
    """ prints each word on seperate line that starts with the given letters, but in all uppercase

        ie. print_upper_words_start(["everyone", "is", "Early", "today"], start_with= ["i", "t"])
                    IS
                    TODAY
    """

    for word in words:
        for char in starts_with:
            if word.startswith(char):
                print(word.upper())
                break
