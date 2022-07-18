# Write a PROGRAM to count the number of vowels in a word.

def validate_input(word):
    """Docstring here"""
    #
    # Your code here
    #
    status = True
    for i in range(0, len(word)):       
        if word[i].isdigit() == True:
            status = False
    return status

def count_vowels(word):
    """Docstring here"""
    #
    # Your code here
    #
    count = 0
    for chr in word:
        if chr.lower() in ('a', 'e', 'i', 'o', 'u'):
            count += 1
    return count

#
if __name__ == "__main__":
    word = input("enter a word: ")
    if validate_input(word) == True:
        print('Vowel = ', count_vowels(word))
    else:
        print("not a word")
   
