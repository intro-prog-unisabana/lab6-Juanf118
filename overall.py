students = {
    "s1":{"assignment1":100, "assignment2":60, "assignment3":80},
    "s2":{"assignment1":60, "assignment2":90, "assignment3":70},
    "s3":{"assignment1":70, "assignment2":80, "assignment3":60}}

def student_averages(students):
    averages = {}
    for student_id, assignments in students.items():
        average = sum(assignments.values()) / len(assignments)
        averages[student_id] = round(average)
    return averages
print(student_averages(students))

def assignment_averages(students):
    assignment_totals = {}
    assignment_prom = {}
    for student_id, assignments in students.items():
        for assignment, score in assignments.items():
            if assignment not in assignment_totals:
                assignment_totals[assignment] = 0
                assignment_prom[assignment] = 0
            assignment_totals[assignment] += score
            assignment_prom[assignment] += 1
    averages = {assignment: (assignment_totals[assignment] / assignment_prom[assignment]) for assignment in assignment_totals}
    return {assignment: round(avg) for assignment, avg in averages.items()}
print(assignment_averages(students))