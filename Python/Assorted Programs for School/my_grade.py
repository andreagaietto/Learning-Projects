from my_grade_class import Grades


def main():
    student1 = Grades()
    lab_grade, mid_grade, final_grade = student1.get_grades()
    weighted = student1.calculate_score(lab_grade, mid_grade,
                                     final_grade)
    print(f"Your final grade is {weighted}")


main()

