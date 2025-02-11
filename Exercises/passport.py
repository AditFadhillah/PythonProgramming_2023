from datetime import date, datetime

class Passport:
    def __init__(self, first_name, last_name, dob, country, exp_date):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()
        self.country = country
        self.exp_date = datetime.strptime(exp_date, "%Y-%m-%d").date()

    def is_valid(self):
        current_date = date.today()
        return self.exp_date > current_date

    def summary(self):
        validity = "valid" if self.is_valid() else "invalid"
        return f"This passport belongs to {self.first_name} {self.last_name}, born on {self.dob} in {self.country}. It is {validity}."

    def check_data(self, first_name, last_name, dob, country):
        return (
            self.first_name == first_name
            and self.last_name == last_name
            and self.dob == datetime.strptime(dob, "%Y-%m-%d").date()
            and self.country == country
            and self.is_valid()
        )

if __name__ == "__main__":
    alan = Passport(
        "Alan",
        "Turing",
        "1912-06-23",
        "The United Kingdom",
        "1954-06-07"
    )

    print(alan.is_valid())
    print(alan.summary())

    codegrade = Passport(
        "Code",
        "Grade",
        "2017-07-21",
        "The Netherlands",
        "2999-12-31"
    )

    print(codegrade.check_data("Code", "Grade", "2017-07-21", "The Netherlands"))
