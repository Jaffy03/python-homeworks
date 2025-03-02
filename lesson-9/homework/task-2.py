import csv

def read_grades(filename):
    grades = [] 
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append(row)
    return grades

def calculate_averages(grades):
    subject_grades = {}
    for entry in grades:
        subject = entry["Subject"]
        grade = int(entry["Grade"])
        if subject in subject_grades:
            subject_grades[subject].append(grade)
        else:
            subject_grades[subject] = [grade]
    
    average_grades = []
    for subject, grades in subject_grades.items():
        average = sum(grades) /len(grades)
        average_grades.append({"Subject": subject, "Average Grade": average})
    return average_grades

def write_averages(filename, average_grades):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Subject', 'Average Grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in average_grades:
            writer.writerow(row)
            
input_file ='grades.csv'
output_file = 'average_grades.csv'
grades = read_grades(input_file)
average_grades = calculate_averages(grades)
write_averages(output_file, average_grades)
print(f"Average grades have been written to {output_file}")

