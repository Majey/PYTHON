while True:
    try:
        number = int(input("Please enter a number: "))
        break # the break forces the program terminate when valid input is entered

    except ValueError:
        print("Please enter an integer")

print(f"Congratulations! { number } is an integer")