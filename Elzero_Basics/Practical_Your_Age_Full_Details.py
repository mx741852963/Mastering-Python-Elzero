# ---------------
# -- Practical Your Age Full Details --
# --------------


# Input

age = int(input("What\'s your Age?").strip())

# Get Age in All time units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(
    f"Your age is {age} years or {months} months or {weeks:,} weeks {days:,} days or {hours:,} hours or {minutes:,} minutes or {seconds:,} seconds")
