text=input("Enter some random sentence: ")
word1=input("Enter a word to be replaced: ")
word2=input("Enter a word to replace with: ")

if word1 in text:
    text=text.replace(word1, word2)
    print(text)
else:
    print(f"{word1} was not found")