def binary_to_decimal(binary_number):
    decimal_number = 0
    power = 0
    while binary_number > 0:
        remainder = binary_number % 10
        decimal_number += remainder * (2 ** power)
        binary_number //= 10
        power += 1
    return decimal_number

def main():
    binary_number = int(input("Enter a binary number: "))
    decimal_number = binary_to_decimal(binary_number)
    print("Decimal equivalent:", decimal_number)

if __name__ == "__main__":
    main()
