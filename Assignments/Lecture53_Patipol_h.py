totalPrice = int(input("Your price: "))

def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

print(vatCalculate(totalPrice))