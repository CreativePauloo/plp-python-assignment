def read_and_modify_file():
    """
    Reads a file, modifies its contents (converts text to uppercase),
    and writes the modified content to a new file.
    """
    try:
        # Get filename from user
        filename = input("Enter the filename to read: ")

        # Open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify content (convert to uppercase)
        modified_content = content.upper()

        # Create a new filename
        new_filename = f"modified_{filename}"

        # Write modified content to a new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been saved to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist! Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied! You don’t have access to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
