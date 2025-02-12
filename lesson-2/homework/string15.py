text=input("Enter some words: ").split()
acronym="".join(word[0].upper() for word in text) 
print(acronym)       