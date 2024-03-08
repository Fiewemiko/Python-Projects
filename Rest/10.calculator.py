def add(n1,n2):
    return n1 + n2
def substract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divided(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divided
}
def calculator():

    first_num = float(input('Enter your first number: '))
    for symbol in operations:
        print(symbol)

    while True:
        operation = input("Pick your operator: ")
        next_num = float(input('Enter your next number: '))
        calc_function = operations[operation]
        result = calc_function(first_num,next_num)
        print(f"{first_num} {operation} {next_num} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            first_num = result
        else:
            calculator()

calculator()