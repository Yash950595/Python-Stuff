import art

#TODO 1: Write out the other 3 functions - subtract, multiply and divide.

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

#TODO 2: Add these 4 functions into a dictionary as the values. Keys = "`+`", "`-`", "`*`", "`/`"

operations={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":div
}

#print variable=operations[*][2,3] 

def calculator():
    print(art.logo)
    store_value = True
    num1 = float(input("What is the first number?: "))

    while store_value:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            store_value = False
            print("\n" * 20)
            calculator()

calculator()