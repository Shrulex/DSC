def print_date(day, year):
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_month = [31, 29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    total_days = day
    month = 0
    while total_days > days_in_month[month]:
        total_days -= days_in_month[month]
        month += 1
    
    return f"{total_days} {months[month]}, {year}"

# Prompt the user for input
try:
    input_day = int(input("Enter the day (1-365): "))
    input_year = int(input("Enter the year: "))
    output = print_date(input_day, input_year)
    print("Output:", output)
except ValueError:
    print("Invalid input. Please enter valid numeric values for day and year.")
