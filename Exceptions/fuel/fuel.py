def main():
    percentage()

def percentage():
    while True:
        try:
            fraction = input("Fraction: ")
            a, b = map(fraction.split("/"))
            if b == 0:  # Prevent ZeroDivisionError
                continue
                
            ans = round(100 * (a / b))

            if ans > 100:
                continue  # Ignore invalid percentages > 100
            elif ans >= 95:
                print("F")
            elif ans <= 10:
                print("E")
            else:
                print(f"{ans}%")
            break  # Exit loop after a valid input
        except (ValueError, ZeroDivisionError, NameError):
            pass  # Ignore errors and prompt again

if __name__ == "__main__":
    main()
