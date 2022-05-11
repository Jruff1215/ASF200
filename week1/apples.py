applePrice = 0.50

name = input("Please enter your name: ")
message_1 = "Hi "+ name +". Apples cost "+ "$" + "{:.2f}".format(applePrice) + " cents each. How many would you like to buy? "
appleAmount = int(input(message_1))
thanks = "Thank you "+ name +" for your purchase of "+ str(appleAmount) + " apples at a cost of " + "$" + "{:.2f}".format(applePrice) +" cents each."
print(appleAmount)
print(thanks)
