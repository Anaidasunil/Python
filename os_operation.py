import os

def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except OSError as e:
        print(f"Error occurred while creating directory '{directory_name}': {e}")

def directory_listing(directory_path):
    try:
        print(f"Listing files and directories in '{directory_path}':")
        for item in os.listdir(directory_path):
            print(item)
    except FileNotFoundError:
        print(f"Directory '{directory_path}' not found.")
    except OSError as e:
        print(f"Error occurred while listing directory '{directory_path}': {e}")

def search_py_files(directory_path):
    try:
        print(f"Searching for '.py' files in '{directory_path}':")
        py_files = [file for file in os.listdir(directory_path) if file.endswith(".py")]
        if py_files:
            for file in py_files:
                print(file)
        else:
            print("No '.py' files found.")
    except FileNotFoundError:
        print(f"Directory '{directory_path}' not found.")
    except OSError as e:
        print(f"Error occurred while searching '.py' files in '{directory_path}': {e}")

def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied to remove file '{file_path}'.")
    except OSError as e:
        print(f"Error occurred while removing file '{file_path}': {e}")

def main():
    # Example usage
    directory_name = "test_directory"
    create_directory(directory_name)

    directory_path = "."  # Current directory
    directory_listing(directory_path)

    search_py_files(directory_path)

    file_to_remove = "test.txt"
    remove_file(file_to_remove)

if __name__ == "__main__":
    main()
