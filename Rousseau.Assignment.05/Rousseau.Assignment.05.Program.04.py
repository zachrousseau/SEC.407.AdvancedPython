# Program #04:

# Use zip function to get the highest grade that the student has achieved and throw out their lowest grade.
# Console
# midterms: [90, 76, 94]
# finals: [78, 79, 90]
# students: ['Marie', 'Michael', 'Marge']
# {'Marie': 90, 'Michael': 79, 'Marge': 94}
# Specifications
# • User zip function. 

def main():
    midterms = [90, 76, 94]
    finals = [78, 79, 90] 
    students = ['Marie', 'Michael', 'Marge'] 

    print(f"\nmidterms: {midterms}")
    print(f"finals: {finals}")
    print(f"students: {students}\n")

    best_grades = {student:max(midterm, final) for student, midterm, final in zip(students, midterms, finals)}
    print(f"{best_grades}")

if __name__ == "__main__":
    main()