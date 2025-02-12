text=input("Enter some random text: ")
digit=False
for i in text:
    if i.isdigit():
        digit=True
if digit:
    print(f"There is a digit")
else:
    print(f"Ther are no digits")     
        
