def initialize_dict(student_name, subject_grades):
    """Parte I: Retorna el diccionario para un solo estudiante."""
    return {student_name: subject_grades}

def add_student(student_grades=None):
    """Parte II: Interacción para agregar un estudiante y sus notas."""
    if student_grades is None:
        student_grades = {}

    name = input("Enter student name:\n").title()
    subjects = {}

    while True:
        entry = input("Enter subject and grade (or 'exit' to finish):\n")
        if entry.lower() == 'exit':
            break
        
        parts = entry.split(',')
        subject = parts[0].strip().title()
        grade = float(parts[1].strip())
        subjects[subject] = grade

    student_grades[name] = subjects
    print(f"Student {name} successfully added to the grades management system.")
    return student_grades

def get_students(student_grades, keys):
    """Parte III: Busca estudiantes ignorando mayúsculas/minúsculas."""
    result = {}
    lookup = {s.lower(): s for s in student_grades.keys()}

    for k in keys:
        search_term = k.lower()
        if search_term in lookup:
            original_name = lookup[search_term]
            result[original_name] = student_grades[original_name]
        else:
            print(f"{k.title()} not found!")
            
    return result

def avg_by_student(student_grades, keys=None):
    """Parte IV: Imprime promedios formateados a 1 decimal."""
    if keys is not None:
        data_to_print = get_students(student_grades, keys)
    else:
        data_to_print = student_grades

    for name, subjects in data_to_print.items():
        if subjects:
            average = sum(subjects.values()) / len(subjects)
            print(f"{name}: {average:.1f}")

