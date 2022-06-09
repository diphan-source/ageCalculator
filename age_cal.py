
""" age_calculator"""

current_year = 2022 # assigning current year to variable current_year

def age_calculator(year_of_birth):
    """
    Calculates the age of a user based on the year of birth
    """
    age = 0
    year_of_birth = int(year_of_birth)
    if year_of_birth > 1900 and year_of_birth < current_year:
        age_value = current_year - year_of_birth
        age += age_value
        print("Your age is  %d yrs" %age)
    else:
        
        print("""please enter your year of birth in the format yyyy.""")
        print("""Enter a year > 1900 : Example: 1994""")
        # return ("Enter valid year")
    
    return age

# requesting user input for year of birth
if __name__ == "__main__":
    year_of_birth = input("Enter your year of birth: ")
    age_calculator(year_of_birth)