def main():
    dollars = float(input("How much was the meal? ").strip().replace("$", ""))
    percent = float(input("What percentage would you like to tip? ").strip().replace("%", "")) / 100
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

main()
