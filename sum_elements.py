# Refactored version of the program to improve readability, structure, and error handling

MAX = 100

def calculate_sum(arr):
    """Calculate the sum of a list of integers."""
    return sum(arr)

def get_number_of_elements():
    """Prompt the user to enter the number of elements and validate the input."""
    while True:
        try:
            n = int(input("Enter the number of elements (1-100): "))
            if 1 <= n <= MAX:
                return n
            else:
                print("Invalid input. Please provide a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_elements(n):
    """Prompt the user to enter n integers and validate each input."""
    arr = []
    print(f"Enter {n} integers:")
    for _ in range(n):
        while True:
            try:
                arr.append(int(input()))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return arr

def main():
    """Main function to execute the program."""
    try:
        n = get_number_of_elements()
        arr = get_elements(n)
        total = calculate_sum(arr)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit(1)

if __name__ == "__main__":
    main()