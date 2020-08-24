from retirement_class import Retiree


def main():

    print("Social Security Full Retirement Age Calculator")
    while True:
        person1 = Retiree()
        birth_year = person1.get_birth_year()
        birth_month = person1.get_birth_month()
        retirement_age, number_months = person1.calculate_receipt_age(
            birth_year)
        final_year, final_month = person1.calculate_retirement_date(
            retirement_age, number_months, birth_year, birth_month)
        print(f"Your full retirement age is {retirement_age} and "
              f"{number_months} months")
        print(f"This will be in {final_month} of {final_year}\n")


main()

