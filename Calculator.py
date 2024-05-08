def calculator():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("\nSelect operation to perform:\n 1.Addition\n 2.Subtraction \n 3.Multiplication \n 4.Division")
    choice = input("Enter your option (1/2/3/4): ")
    if choice == '1':
        print('Answer:',num1+num2)
    elif choice == '2':
        print('Answer:',num1-num2)
    elif choice == '3':
        print('Answer:',num1*num2)
    else:
        try:
            print('Answer:',num1/float(num2))
        except ZeroDivisionError:
            print("Error! Division by zero is not allowed.")
            return calculator()

if __name__ == '__main__':
    while True:
        calculator()