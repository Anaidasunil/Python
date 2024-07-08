def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)
        print(f"Contents of {source_file} copied successfully to {destination_file}.")
    except FileNotFoundError:
        print("One of the files does not exist. Please check the file paths.")
    except IOError:
        print("Error occurred while reading/writing files.")

def main():
    source_file = input("Enter the path of the source file: ")
    destination_file = input("Enter the path of the destination file: ")

    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()
