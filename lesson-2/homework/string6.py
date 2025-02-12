text=input("Enter some random text: ")
text2=input("Enter a text to check if it is in first text: ")
if text2 in text:
    print(f"{text2} was found")
else:
    print(f"{text2} was not found")