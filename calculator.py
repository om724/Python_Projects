try:
    a= int(input("Enter The First Number :"))

    b= int(input("Enter The Sceond Number : "))

    print("what kind of operation do you want to perfrom .\n Press + for addition \n Press - for substraction \n Press * for multiplication \n Press / for division ")

    o = input("Enter Operation:")

    match o:
        case "+":
            print(f"The Result is :{a+b}")

        case "-":
            print(f"The Result is:{a-b}")

        case "*":
            print(f"The Result is:{a*b}")

        case "/":
            print(f"The Result is:{a/b}")


except Exception as e:
    print("Enter a valid value of a and b")

