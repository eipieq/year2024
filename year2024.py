from datetime import datetime, timedelta

def calculate_percentage_and_hours_of_year_passed(target_year=2024):
    current_datetime = datetime.now()

    # Calculate the total number of 30-minute intervals in a standard and leap year
    standard_year_intervals = 365 * 24 * 2
    leap_year_intervals = 366 * 24 * 2

    # Check if the target year is a leap year
    if current_datetime.year == target_year and (
        (current_datetime.year % 4 == 0 and current_datetime.year % 100 != 0) or
        (current_datetime.year % 400 == 0)
    ):
        total_intervals_in_year = leap_year_intervals
    else:
        total_intervals_in_year = standard_year_intervals

    # Calculate the number of 30-minute intervals passed in the current year
    seconds_passed = (current_datetime - datetime(current_datetime.year, 1, 1)).total_seconds()
    intervals_passed = seconds_passed / 1800

    # Calculate the percentage of the year passed
    percentage_passed = (intervals_passed / total_intervals_in_year) * 100

    # Calculate the number of hours passed
    hours_passed = seconds_passed / 3600

    return percentage_passed, hours_passed

# Example usage
percentage_passed, hours_passed = calculate_percentage_and_hours_of_year_passed()
print(f"Number of hours passed in 2024: \033[1m{hours_passed:.2f}\033[0m")
print(f"Percentage of the year passed in 2024: \033[1m{percentage_passed:.2f}%\033[0m")