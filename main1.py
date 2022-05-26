# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


# work only with words
def find_anagram(word, anagram):
    # [assignment] Add your code here
    # check the length of words and anagram
    # using .replace(" ", "") in case the anagram is a sentence
    len_word = len(word.replace(" ", ""))
    # print(len_word)
    anagram_len = len(anagram.replace(" ", ""))
    # print(anagram_len)
    if(len_word != anagram_len):
        return False
    if(len_word == anagram_len):
        # check the letters of words and anagram
        # print("same length")
        split_word = list(word)
        # print(split_word)
        anagram_split = list(anagram)
        # print(anagram_split)
        for letter in split_word:
            # print(letter)
            if letter not in anagram:
                return False

    
    # check the letters of words and anagram

    return True


# manual check
answer = find_anagram("below", "elbow")
print(answer)

# check using user input
input_word = input("Enter word: ")
input_anagram = input("Enter anagram: ")
check = find_anagram(input_word, input_anagram)
print(check)