age =int(input("Enter Your Age\n"))
year_remaining= 90-age
months_remaining=year_remaining*12
days_remaining = 365*year_remaining
weeks_remaining= 52*year_remaining
print(f"YOu have {days_remaining} days ,  {weeks_remaining} weeks ,  {months_remaining} months left")