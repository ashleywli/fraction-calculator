def menu():
    print("This program performs operations on fractions. Enter")
    print("1: To add fraction")
    print("2: To subtract fraction")
    print("3: To multiply fraction")
    print("4: To divide fraction")
    print("9: To exit the program")

def fractionlol(fraction_number):
    print(f"For fraction {fraction_number}")
    while True:
        numerator = input("Enter the numerator: ")
        denominator = input("Enter the denominator: ")
        if numerator.isdigit() and denominator.isdigit():
            denominator = int(denominator)
            if denominator != 0:
                return int(numerator), denominator
        print("The denominator must be nonzero.")

def add_fractions(fraction1, fraction2):
    num1, denom1 = fraction1
    num2, denom2 = fraction2
    result_num = num1 * denom2 + num2 * denom1
    result_denom = denom1 * denom2
    return result_num, result_denom

def subtract_fractions(fraction1, fraction2):
    num1, denom1 = fraction1
    num2, denom2 = fraction2
    result_num = num1 * denom2 - num2 * denom1
    result_denom = denom1 * denom2
    return result_num, result_denom

def multiply_fractions(fraction1, fraction2):
    num1, denom1 = fraction1
    num2, denom2 = fraction2
    result_num = num1 * num2
    result_denom = denom1 * denom2
    return result_num, result_denom

def divide_fractions(fraction1, fraction2):
    num1, denom1 = fraction1
    num2, denom2 = fraction2
    if num2 == 0:
        print("To divide, the second fraction must be nonzero.")
        return None
    result_num = num1 * denom2
    result_denom = denom1 * num2
    return result_num, result_denom

def main():
    while True:
        menu()
        choice = input()
        if choice == '9':
            break
        fraction1 = fractionlol(1)
        fraction2 = fractionlol(2)
        if choice == '1':
            result = add_fractions(fraction1, fraction2)
            print(f"{fraction1[0]}/{fraction1[1]} + {fraction2[0]}/{fraction2[1]} = {result[0]}/{result[1]}")
        elif choice == '2':
            result = subtract_fractions(fraction1, fraction2)
            print(f"{fraction1[0]}/{fraction1[1]} - {fraction2[0]}/{fraction2[1]} = {result[0]}/{result[1]}")
        elif choice == '3':
            result = multiply_fractions(fraction1, fraction2)
            print(f"{fraction1[0]}/{fraction1[1]} * {fraction2[0]}/{fraction2[1]} = {result[0]}/{result[1]}")
        elif choice == '4':
            result = divide_fractions(fraction1, fraction2)
            if result:
                print(f"{fraction1[0]}/{fraction1[1]} / {fraction2[0]}/{fraction2[1]} = {result[0]}/{result[1]}")

main()
