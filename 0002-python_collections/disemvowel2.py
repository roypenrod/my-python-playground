# takes a string
# returns a string without the vowels in it
# y is not consider a vowel
def remove_vowels(string):
    # list of vowels to check for
    vowel_list = list("aeiou")

    # split the string into a list of characters
    char_list = list(string.lower())

    # iterate through the vowels
    for vowel in vowel_list:
        # set up an infinite loop
        while True:
            # try to remove the vowel from char_list
            # if it throws an error, break out of
            # infinite loop
            try:
                char_list.remove(vowel)
            except:
                break

    # return the joined char_list
    return ''.join(char_list)


# Test
state_names = ["Alabama", "California", "Florida", "Oklahoma", "Utah"]


for state in state_names:
    print(" ")
    print(state + ": ")
    consonants = remove_vowels(state)
    print("consonants: " + consonants)
