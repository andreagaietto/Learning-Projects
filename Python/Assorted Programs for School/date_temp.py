from date_temp_class import DateTemp
object_list = []


def main():
    # controls general flow of program by user selection. Creates
    # new object, adding object to a list for later use
    creation_number = 0
    to_continue = "y"
    while to_continue != "n":
        selection = select_option()
        if selection == 1:
            creation_number += 1
            new_info = DateTemp(creation_number)
            object_list.append(new_info)
            new_info.get_date()
            new_info.get_temp()
            print("\nYou have entered the following:")
            print(new_info)
        elif selection == 2:
            by_order_created()
        elif selection == 3:
            by_date()
        elif selection == 4:
            by_temperature()
        else:
            to_continue = "n"


def select_option():
    # validates that a valid option is selected
    print("\nWhat would you like to do? Please select from the "
          "following list of options:")
    print("1. Enter a date and temperature")
    print("2. Display all date and temperature information in "
          "the order entered")
    print("3. Display all date and temperature information by "
          "date")
    print("4. Display all date and temperature information by "
          "temperature")
    print("5. Exit")
    while True:
        try:
            selection = int(input("Please enter your selection: "))
            if selection < 1 or selection > 5:
                raise()
            else:
                return selection
        except:
            print("Please enter a valid selection.")


def by_order_created():
    # create and print a list sorted by order created
    order_created_list = sorted(object_list,
                                key=lambda x: x.creation_number)
    print(order_created_list)


def by_date():
    # create and print a list sorted by date
    by_date_list = sorted(object_list, key=lambda x: x.date)
    print(by_date_list)


def by_temperature():
    # create and print a list sorted by temperature
    by_temp_list = sorted(object_list, key=lambda x: x.temp)
    print(by_temp_list)


main()
