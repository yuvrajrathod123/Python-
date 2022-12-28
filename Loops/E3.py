
# Program that accepts a word from the user and reverse it

word = str(input("Enter the word to be reverse: "))

for char in range(len(word)-1, -1, -1):
    print(word[char], end=" ")
print("\n")