class Retiree:

    def __init__(self):

        self.month_dict = {1: "January", 2: "February", 3: "March",
                      4: "April",
                      5: "May", 6: "June", 7: "July", 8: "August",
                      9: "September", 10: "October", 11: "November",
                      12: "December"}

    def get_birth_year(self):
        while True:
            choice = input("Please enter the year of your birth or hit "
                           "return to exit: ")
            if not choice:
                exit()
            try:
                year = int(choice)
                if year < 1900 or year > 2020:
                    raise ()
                return year
            except:
                print("Invalid input.")

    def get_birth_month(self):
        while True:
            try:
                month = int(input("Please enter the month of your birth (number 1-12): "))
                if month < 1 or month > 12:
                    raise()
                return month
            except:
                print("Invalid input.")

    def calculate_receipt_age(self, year):
        if year <= 1937:
            age = 65
            months = 0
        elif 1938 <= year <= 1942:
            age = 65
            months = (year - 1937) * 2
        elif 1943 <= year <= 1954:
            age = 66
            months = 0
        elif 1955 <= year <= 1959:
            age = 66
            months = (year - 1954) * 2
        else:
            age = 67
            months = 0
        return age, months

    def calculate_retirement_date(self, retirement_age, number_months,
                                  birth_year, birth_month):
        final_year = retirement_age + birth_year
        month_count = number_months + birth_month
        if month_count > 12:
            final_year += 1
            month_count -= 12
        final_month = self.month_dict[month_count]
        return final_year, final_month
