end = input("Please enter a positive number: ")
running = True
while running: 
    if end.isdigit() == True:

        for number in range(0, int(end) +1):
            if number % 2 == 0:
                print(number, end = " ")
        running = False
    else: 
        print("Invalid input. Please enter a positive number: " + end)
        end = input("Please enter a positive number: ")
