

usernameInput = input("Username: ")
password = input("Password: ")

if usernameInput == ("patipol") and password == ("7979"):
    print("Welcome to IT Shop!")
    print(" สินค้า                      ราคา")
    print("1.Ram      :         2,000 THB")
    print("2.Mouse    :           250 THB")
    print("3.Keyboard :           599 THB")

    usernameInput = int(input("เลขสินค้าที่ต้องการ : "))
    if usernameInput == 1:
        print("Ram")
        Ram = int(input("จำนวนที่ต้องการ: "))
        price = int(2000)
        result = Ram * price
        print(result,"THB")
    elif usernameInput == 2:
        print("Mouse")
        Mouse = int(input("จำนวนที่ต้องการ: "))
        price = int(250)
        result = Mouse * price
        print(result,"THB")
    elif usernameInput == 3:
        print("Keyboard")
        Keyboard = int(input("จำนวนที่ต้องการ: "))
        price = int(599)
        result = Keyboard * price
        print(result,"THB")
