text=input("Enter a text: ")
text1=text.lower()
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
vowel_count=0
consonant_count=0
for i in text1:
    if i in vowels:
        vowel_count+=1
    if i in consonants:
        consonant_count+=1
print(f"There are {vowel_count} vowels")
print(f"There are {consonant_count} consonants")