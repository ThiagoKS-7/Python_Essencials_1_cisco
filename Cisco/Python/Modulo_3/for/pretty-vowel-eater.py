# Prompt the user to enter a word
# and assign it to the user_word variable.
word = input("Enter a word: ")
word = word.upper()
vowels = ['A', 'E', 'I', 'O', 'U']

for letter in word:
    if letter in vowels:
        continue;
    print(letter)
    # Complete the body of the for loop.
