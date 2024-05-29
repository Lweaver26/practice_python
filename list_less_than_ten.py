def lessThanFive(list):
    smallerThanNumber = input("Please enter a number: ")
    newlist = [number for number in list if number < int(smallerThanNumber) ]
    print(newlist)

        
lessThanFive([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
    

    