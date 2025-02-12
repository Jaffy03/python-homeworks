text=input("Enter some text to check: ")
text=text.lower()
match=True
length=len(text)
count=0
for i in text:
    count+=1
    if i != text[length-count]:
        match=False
        print(f"{text} is not palyndrome")
        break
    
if match:
    print(f"{text} is palyndrome")