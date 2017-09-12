import re

def check_letters(text):

    my_string = only_letters(text)
    max_value = get_higher_occurence(list_of_occurences(my_string))
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

    #local testing

    assert check_letters("H.P.Lovecraft") == "a", "Start"

    assert check_letters("How about this one?") == "o", "O is most wanted"

    assert check_letters("One") == "e", "All letter only once."

    assert check_letters("Oops!") == "o", "Lower case."

    assert check_letters("AAaooo!!!!") == "a", "Only letters."

    assert check_letters("abe") == "a", "The First."

    print("Start the long test")

    assert check_letters("a" * 9000 + "b" * 1000) == "a", "Very long."

    print("The local tests are done.")

