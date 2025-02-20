universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(lst):
    students=[]
    tuition=[]
    for uni in lst:
        students.append(uni[1])
        tuition.append(uni[2])
    return students, tuition

def mean(lst):
    return sum(lst)/len(lst)

def median(lst):
    lst.sort()
    if len(lst)%2==0:
        return (lst[len(lst)//2]+lst[len(lst)//2-1])/2
    else:
        return lst[len(lst)//2]

try:
    students, tuition=enrollment_stats(universities)

    total_students = sum(students)
    total_tuition = sum(tuition)
    student_mean = mean(students)
    student_median = median(students)
    tuition_mean = mean(tuition)
    tuition_median = median(tuition)

    print("******************************")
    print(f"Total students: {total_students:,}")
    print(f"Total tuition: $ {total_tuition:,}\n")
    print(f"Student mean: {student_mean:,.2f}")
    print(f"Student median: {student_median:,.0f}\n")
    print(f"Tuition mean: $ {tuition_mean:,.2f}")
    print(f"Tuition median: $ {tuition_median:,.0f}")
    print("******************************")
except:
    "Entered values are not correct"