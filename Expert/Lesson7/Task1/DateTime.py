from datetime import datetime

def validate(value: str)->bool:
    try:
        date = datetime.strptime(value, "%d.%m.%Y")

        if value != date.strftime("%d.%m.%Y"):
            raise ValueError

        if _isleap(date.year):
            print("Year is leap!")
        else:
            print("Year not leap!")

        return True
    except ValueError:
        return False

def _isleap(year: int)->bool:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    if validate("01.01.2000"):
        print("Date is correct!")
    else:
        print("Date is wrong!")

    if _isleap(2000):
        print("Year is leap!")
    else:
        print("Year not leap!")