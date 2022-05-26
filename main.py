# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

# to check the length of a string without counting any space included
# text = "nag a ram"
# txt_len = len(text.replace(" ", ""))
# print(txt_len)
# print(len("nagaram"))


def find_anagram(word, anagram):
    # [assignment] Add your code here
    # check the length of words and anagram
    # using .replace(" ", "") in case the anagram is a sentence
    len_word = len(word.replace(" ", ""))
    anagram_len = len(anagram.replace(" ", ""))
    if(len_word != anagram_len):
        return False
    if(len_word == anagram_len):
        # check the letters of words and anagram
        # making sure the letters present in words and anagram are the same
        split_word = list(word)
        anagram_split = list(anagram)
        for letter in split_word:
            # if letters are not in anagram
            if letter not in anagram:
                # if the letters are not present return false
                return False
    # if letters are present in both words and anagram
    return True

# check using user input
input_word = input("Enter word: ")
input_anagram = input("Enter anagram: ")
check = find_anagram(input_word, input_anagram)
print(check)

