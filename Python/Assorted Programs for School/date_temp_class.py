import datetime


class DateTemp:

    def __init__(self, creation_number):
        # initialize
        self.creation_number = creation_number
        self.temp = 0
        self.day = None
        self.month = None
        self.year = None
        self.date = None

    def get_date(self):
        # call each function that is needed and validates if correct
        # input in order, as well as checks if a date exists on the
        # calendar
        while True:
            try:
                self.get_year()
                self.get_month()
                self.get_day()
                self.date = datetime.date(int(self.year),
                                       int(self.month),
                                  int(self.day))
                return
            except ValueError:
                print("Date entered does not exist. Please enter a "
                      "valid date.")

    def get_year(self):
        # obtain year
        while True:
            try:
                self.year = int(input("Please provide a four digit "
                                  "year: "))
                if self.year < 1000 or self.year > 9999:
                    raise()
                else:
                    return
            except:
                print("Invalid input.")

    def get_month(self):
        # obtain month
        while True:
            try:
                self.month = input("Please provide a two "
                                          "digit "
                                       "month: ")
                if len(self.month) != 2:
                    raise()
                if int(self.month) < 1 or int(
                        self.month) > 12:
                    raise()
                else:
                    return
            except:
                print("Invalid input.")

    def get_day(self):
        # obtain day
        while True:
            try:
                self.day = input("Please provide a two digit day: ")
                if len(self.day) != 2:
                    raise()
                if int(self.day) < 1 or int(self.day) > 31:
                    raise()
                else:
                    return
            except:
                print("Invalid input.")

    def get_temp(self):
        # obtain temperature
        while True:
            try:
                self.temp = int(input("Please provide a "
                                      "temperature no greater than "
                                      "three digits, with no "
                                      "decimals: "))
                if len(str(self.temp)) > 3:
                    raise()
                else:
                    return
            except:
                print("Invalid input.")

    def __repr__(self):
        # determine what will be returned if object is referred to
        return repr(f"{self.date}, {self.temp} degrees")
