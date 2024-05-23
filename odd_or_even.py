def odd_or_even():
    number = int(input("Please enter a number: "))
    if number % 4 == 0:
        print(f"The number you selected: {number}, is a multiple of 4!")
    elif number % 2 == 0:
        print(f"The number you selected: {number}, is an even number!")
    elif number % 2 != 0:
        print(f"The number you selected: {number}, is an odd number!")

odd_or_even()