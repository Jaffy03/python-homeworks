text=input("Enter some text: ")
vowels="aeiouAEIOU"
for i in text:
    if i in vowels:
        text=text.replace(i, '*')
print(f"Inserted text, vowels replaced by '*': {text}")