import re

def checkio(text):

    my_string = only_letters(text)

    max_value = get_higher_occurence(list_of_occurences(my_string))

    #replace this for solution

    my_letters = check_equal_occurences(list_of_occurences(my_string), max_value)

    return get_firs_letter(my_letters)

def only_letters(string):

    return re.sub('[^a-zA-Z]+', '', string)

def list_of_occurences(text):

    occurences = dict()

    for i in text:

        i = i.lower()

        if i not in occurences:

            occurences[i] = 1

        else:

            occurences[i] += 1    

    return occurences

def get_higher_occurence(dictionary):

    return  max(dictionary.values()) 

def check_equal_occurences(dictionary, maximum):

    equals = []

    for letter, value in dictionary.items():

        if value == maximum:

            equals.append(letter)

    return equals

def get_firs_letter(letters):

    return sorted(letters)[0]

if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert checkio("H.P.Lovecraft") == "a", "Start"

    assert checkio("How about this one?") == "o", "O is most wanted"

    assert checkio("One") == "e", "All letter only once."

    assert checkio("Oops!") == "o", "Lower case."

    assert checkio("AAaooo!!!!") == "a", "Only letters."

    assert checkio("abe") == "a", "The First."

    print("Start the long test")

    assert checkio("a" * 9000 + "b" * 1000) == "a", "Very long."

    print("The local tests are done.")

