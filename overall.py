my_dict = {
    "student_id1":{"assignment1":100, "assignment2":90, "assignment3":80},
    "student_id2":{"assignment1":90, "assignment2":80, "assignment3":70},
    "student_id3":{"assignment1":80, "assignment2":70, "assignment3":60}
}
def student_averages(my_dict):
    averages = {}
    for student_id, assignments in my_dict.items():
        average = sum(assignments.values()) / len(assignments)
        averages[student_id] = average
    return averages
print(student_averages(my_dict))

def assignments_average(my_dict):
    assignment_totals = {}
    assignment_prom = {}
    for student_id, assignments in my_dict.items():
        for assignment, score in assignments.items():
            if assignment not in assignment_totals:
                assignment_totals[assignment] = 0
                assignment_prom[assignment] = 0
            assignment_totals[assignment] += score
            assignment_prom[assignment] += 1
    averages = {assignment: assignment_totals[assignment] / assignment_prom[assignment] for assignment in assignment_totals}
    return averages
print(assignments_average(my_dict))