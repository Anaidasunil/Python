def check_substring(s1, s2):
    if s2 in s1:
        return True
    else:
        return False

def count_occurrences(s, c):
    return s.count(c)

def replace_substring(s, old, new):
    return s.replace(old, new)

def convert_to_capital(s):
    return s.upper()

def main():
    while True:
        print("String Operations Menu:")
        print("1. Check if a string is a substring of another string")
        print("2. Count occurrences of a character in a string")
        print("3. Replace a substring with another substring")
        print("4. Convert a string to capital letters")
        print("5. Quit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            s1 = input("Enter the main string: ")
            s2 = input("Enter the substring to check: ")
            if check_substring(s1, s2):
                print(f"'{s2}' is a substring of '{s1}'")
            else:
                print(f"'{s2}' is not a substring of '{s1}'")
        elif choice == 2:
            s = input("Enter the string: ")
            c = input("Enter the character to count: ")
            count = count_occurrences(s, c)
            print(f"The character '{c}' occurs {count} times in '{s}'")
        elif choice == 3:
            s = input("Enter the string: ")
            old = input("Enter the substring to replace: ")
            new = input("Enter the new substring: ")
            result = replace_substring(s, old, new)
            print(f"Replacing '{old}' with '{new}' in '{s}' gives: {result}")
        elif choice == 4:
            s = input("Enter the string: ")
            result = convert_to_capital(s)
            print(f"The capital version of '{s}' is: {result}")
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
