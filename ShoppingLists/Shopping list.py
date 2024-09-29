import os

# Function to get all .txt files in the specified directory
def get_text_files(directory_path):
    # List comprehension to return all files ending with '.txt'
    return [f for f in os.listdir(directory_path) if f.endswith(".txt")]

# Function to create or manage a shopping list
def create_shopping_list():
    shopping_list = []  # Initialize an empty list to store shopping items

    # Path to the directory where shopping lists will be saved
    directory_path = r"C:\Users\fese\OneDrive\Documents\GitHub\Python\Good\ShoppingLists"

    # Check if the directory exists, if not, create it
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)  # Create directory if it doesn't exist

    # Get all text files (existing shopping lists) from the directory
    text_files = get_text_files(directory_path)

    # If there are no text files in the directory, exit the program
    if not text_files:
        print("No text files found in the directory. Exiting.")
        return

    # Present options to the user
    print("Choose an option:")
    print("1. Continue with an existing list")
    print("2. Create a new list")
    print("3. Delete an existing list and create a new one")

    # Get the user's choice
    choice = input("Enter 1, 2, or 3: ")

    # Option 1: Continue with an existing list
    if choice == '1':
        print("Existing text files:")

        # Display the existing text files (shopping lists)
        for i, text_file in enumerate(text_files, start=1):
            print(f"{i}. {text_file}")

        # Let the user choose which list to continue
        list_choice = int(input("Enter the number of the list you want to continue: ")) - 1
        file_path = os.path.join(directory_path, text_files[list_choice])  # Get the path of the selected file

    # Option 2: Create a new list
    elif choice == '2':
        # Ask the user if they want to name the new shopping list
        custom_name_choice = input("Do you want to enter a custom name for the new list? (yes/no): ").lower()

        # If yes, ask for a custom name and create the new list with that name
        if custom_name_choice == 'yes':
            shopping_list_name = input("Enter a name for the new shopping list: ")
            file_path = os.path.join(directory_path, f"{shopping_list_name}.txt")  # Set file path with custom name
        else:
            # If no, automatically name the new list based on the number of existing lists
            list_number = len(text_files) + 1
            shopping_list_name = f"shoppinglist{list_number}"  # Generate a default list name
            file_path = os.path.join(directory_path, f"{shopping_list_name}.txt")

    # Option 3: Delete an existing list and create a new one
    elif choice == '3':
        print("Existing text files:")

        # Display the existing text files (shopping lists)
        for i, text_file in enumerate(text_files, start=1):
            print(f"{i}. {text_file}")

        # Let the user choose which list to delete
        list_choice = int(input("Enter the number of the list you want to delete and create a new one: ")) - 1
        file_to_delete = os.path.join(directory_path, text_files[list_choice])  # Get the path of the file to delete
        os.remove(file_to_delete)  # Delete the selected file
        print(f"{text_files[list_choice]} deleted.")  # Inform the user that the file was deleted

        # Ask if the user wants to name the new shopping list
        custom_name_choice = input("Do you want to enter a custom name for the new list? (yes/no): ").lower()

        # If yes, ask for a custom name and create the new list with that name
        if custom_name_choice == 'yes':
            shopping_list_name = input("Enter a name for the new shopping list: ")
            file_path = os.path.join(directory_path, f"{shopping_list_name}.txt")
        else:
            # If no, automatically name the new list based on the number of remaining lists
            list_number = len(text_files) + 1
            shopping_list_name = f"shoppinglist{list_number}"
            file_path = os.path.join(directory_path, f"{shopping_list_name}.txt")

    # If an invalid choice is entered, exit the program
    else:
        print("Invalid choice. Exiting.")
        return

    # Loop to add items to the shopping list until the user finishes
    while True:
        # Prompt the user to enter an item
        item = input("Enter an item to add to your shopping list (press Enter to finish, type '%%**' to exit): ")

        # If the user presses Enter without typing anything, finish adding items
        if not item:
            break

        # If the user enters '%%**', stop adding items and exit
        if item == "%%**":  # Word to end list
            break

        shopping_list.append(item)  # Add the item to the shopping list

    # Write the shopping list to the file
    with open(file_path, "w") as file:
        for item in shopping_list:
            file.write(f"{item}\n")  # Write each item on a new line

    # Inform the user that the shopping list has been created successfully
    print(f"Shopping list created successfully! Check '{file_path}'.")

# Call the create_shopping_list function if the script is run directly
if __name__ == "__main__":
    create_shopping_list()
