from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day)
    )
    return age

def main():
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(dob_input, "%Y-%m-%d")
        age = calculate_age(birthdate)
        if age < 18:
            print("Under age")
        else:
            print(f"Your age is: {age}")
    except ValueError:
        print("Invalid date format. Please enter in YYYY-MM-DD format.")

main()
