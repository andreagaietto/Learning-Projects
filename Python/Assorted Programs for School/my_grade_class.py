class Grades:

    def __init__(self):

        self.lab_weight = 34
        self.mid_weight = 33
        self.final_weight = 33

    def get_grades(self):
        labs = self.get_number_input(
            "Please provide your total earned "
            "points for labs: ")
        midterm = self.get_number_input(
            "Please provide your total earned points "
            "for the midterm: ")
        final = self.get_number_input(
            "Please provide your total earned points "
            "for the final: ")
        return labs, midterm, final

    def get_number_input(self,phrase):
        while True:
            try:
                grade = float(
                    input(phrase))
                return grade
            except ValueError:
                print("Invalid input.")

    def calculate_score(self, lab_grade, mid_grade, final_grade):
        weighted_lab = (lab_grade * self.lab_weight) / 100
        weighted_midterm = (mid_grade * self.mid_weight) / 100
        weighted_final = (final_grade * self.final_weight) / 100
        weighted_total = weighted_lab + weighted_midterm + weighted_final
        return weighted_total
