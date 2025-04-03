def odd_even_checker(number):
    return "The number is even." if number % 2 == 0 else "The number is odd."

def main():
    number = int(input("Enter a number: "))
    print(odd_even_checker(number))

if __name__ == "__main__":
    main()