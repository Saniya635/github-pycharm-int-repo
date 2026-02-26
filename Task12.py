#Lab Assignment 1
string = input("Enter a sentence: ")
vowels = 0
consonants = 0
spaces = 0
lowercase = 0
vowel_letters = "aeiouAEIOU"
for ch in string:
    if ch == " ":
        spaces += 1
    if ch.islower():
        lowercase += 1
    if ch.isalpha():
        if ch in vowel_letters:
            vowels += 1
        else:
            consonants += 1
print("\n--- String Statistics ---")
print("Number of vowels =", vowels)
print("Number of consonants =", consonants)
print("Number of spaces =", spaces)
print("Number of lowercase letters =", lowercase)


#Lab Assignment 2
def make_capital(sentence):
    result = sentence.upper()
    return result
line = input("Enter a line: ")
output = make_capital(line)
print("Capitalized sentence is:")
print(output)