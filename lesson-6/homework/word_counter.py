import string
import os

def input_file():
    sample = input("Type a paragraph to create a file:\n")
    with open('sample.txt', 'w') as file:
        file.write(sample)
    print("File 'sample.txt' has been created.\n")

def count_words(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

def report(word_count, total_words):
    n= int(input("Enter how many top comment words to display: "))
    sorted_words = sorted(word_count.items(), key = lambda x: x[1], reverse=True)
    
    print(f'Total words: {total_words}')
    print(f'Top {n} most common words:')
    for word, count in sorted_words[:n]:
        print(f'{word} - {count} times')
    
    with open("word_count_report.txt", 'w') as report_file:
        report_file.write("Word Count Report\n")
        report_file.write(f"Totat Words: {total_words}\n")
        report_file.write(f"Top {n} Words:\n")
        for word, count in sorted_words[:n]:
            report_file.write(f'{word} - {count}\n')
    print("\nReport saved to 'word_count_report.txt'.")

if not os.path.exists("sample.txt"):
    input_file()

with open('sample.txt') as file:
    content = file.read()

word_count = count_words(content)
total_words = sum(word_count.values())

report(word_count, total_words)    