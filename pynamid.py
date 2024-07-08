def print_pyramid(levels):
    for i in range(1, levels + 1):
        # Print leading spaces
        for j in range(levels - i):
            print(" ", end="")

        # Print numbers in ascending order
        for j in range(1, i + 1):
            print(j, end="")

        # Print numbers in descending order
        for j in range(i - 1, 0, -1):
            print(j, end="")

        # Move to the next line
        print()

def main():
    try:
        levels = int(input("Enter the number of levels for the pyramid: "))
        if levels < 1:
            raise ValueError("Number of levels should be a positive integer.")
    except ValueError as e:
        print(e)
        return

    print_pyramid(levels)

if __name__ == "__main__":
    main()
