import grades_manager

def main():
    print("Welcome to the Student Grades Manager!")
    my_grades = {}

    while True:
        print("\nSelect an option:")
        print("1. Add a student")
        print("2. Print student grade averages")
        print("3. Exit")
        
        choice = input()

        if choice == '1':
            my_grades = grades_manager.add_student(my_grades)
        
        elif choice == '2':
            print("Select an option:")
            print("a. Display all students")
            print("b. Display selected students")
            sub_choice = input().lower()

            if sub_choice == 'a':
                grades_manager.avg_by_student(my_grades)
            elif sub_choice == 'b':
                names_raw = input("Enter student names (comma-separated):\n")
                names_list = [n.strip() for n in names_raw.split(',')]
                grades_manager.avg_by_student(my_grades, names_list)
            else:
                print("Invalid option selected!")
        
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option selected!")

if __name__ == "__main__":
    main()