def is_leap_year(year):

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print("=" * 40)
print("LEAP YEAR CHECKER")
print("=" * 40)

while True:
    try:
        year = int(input("\nEnter a year: "))

        if year <= 0:
            print("Please enter a valid positive year.")
            continue

        if is_leap_year(year):
            print(f"\n✅ {year} is a Leap Year.")
        else:
            print(f"\n❌ {year} is NOT a Leap Year.")

        choice = input("\nDo you want to check another year? (yes/no): ").lower()

        if choice != "yes":
            print("\nThank you for using Leap Year Checker!")
            break

    except ValueError:
        print("Invalid input! Please enter numbers only.")