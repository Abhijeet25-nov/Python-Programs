def calculate_minutes(age_years):
    DAYS_IN_YEARS=365.25
    HOURS=24
    MINUTES_IN_HOUR=60
    
    total_days=age_years*DAYS_IN_YEARS
    total_hours=HOURS*total_days
    total_minutes=MINUTES_IN_HOUR*total_hours
    
    return (round(total_days),round(total_hours),round(total_minutes))

while True:
    try:
        age=float(input("Enter your age in years: "))
        days, hours, minutes=calculate_minutes(age)
        
        print("\n You are approx:")
        print(f" - {days} days old")
        print(f" - {hours} hours old")
        print(f" - {minutes} minutes old")
        
        again=input("Would you try again: (y/n) ").strip().lower()
        
        if again !="y":
            print("Good Bye")
            break
    
    except:
        print("Please enter a valid number for age")    