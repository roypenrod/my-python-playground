# takes a string
# returns a string without the vowels in it
# y is not consider a vowel
def remove_vowels(string):
    # list of vowels to check for
    vowel_list = ["a", "e", "i", "o", "u"]

    # split the string into a list of characters
    char_list = list(string.lower())

    # create an empty list to hold the consonants
    consonant_list = []

    # iterate through char_list and remove
    # each vowel from vowel_list
    for char in char_list:
        # flag for tracking if char == vowel
        is_vowel = False

        # iterate through vowel_list
        for vowel in vowel_list:
            # if the char is a vowel,
            # set is_vowel flag to True
            if (char == vowel):
                is_vowel = True
                break

        # check to see if is_vowel == False
        # if is_vowel == False, add it to consonant_list
        if is_vowel == False:
            consonant_list.append(char)

    #join the consonants left in char_list
    # into a string and return it
    return ''.join(consonant_list)



# Test
state_names = ["Alabama", "California", "Florida", "Oklahoma", "Utah"]


for state in state_names:
    print(" ")
    print(state + ": ")
    consonants = remove_vowels(state)
    print("consonants: " + consonants)
