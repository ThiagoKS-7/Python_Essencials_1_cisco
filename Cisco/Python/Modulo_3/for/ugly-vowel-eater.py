# Prompt the user to enter a word
# and assign it to the user_word variable.
word = input("Enter a word: ")
word = word.upper()

for letter in word:
    if letter =='A' or  letter =='E' or  letter =='I' or  letter =='O' or  letter =='U':
        continue;
    print(letter)
    # Complete the body of the for loop.
