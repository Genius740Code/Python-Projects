import os

def get_text_files(directory_path):
    return [f for f in os.listdir(directory_path) if f.endswith(".txt")]

def create_shopping_list():
    shopping_list = []

    directory_path = r"C:\Users\fese\OneDrive\Documents\GitHub\Python\Good\ShoppingLists"

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    text_files = get_text_files(directory_path)

    if not text_files:
        print("No text files found in the directory. Exiting.")
        return

    print("Choose an option:")
    print("1. Continue with an existing list")
    print("2. Create a new list")
    print("3. Delete an existing list and create a new one")

    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        print("Existing text files:")
        for i, text_file in enumerate(text_files, start=1):
            print(f"{i}. {text_file}")

        list_choice = int(input("Enter the number of the list you want to continue: ")) - 1
        file_path = os.path.join(directory_path, text_files[list_choice])

    elif choice == '2':
        custom_name_choice = input("Do you want to enter a custom name for the new list? (yes/no): ").lower()

        if custom_name_choice == 'yes':
            shopping_list_name = input("Enter a name for the new shopping list: ")
            file_path = os.path.join(directory_path, f"{shopping_list_name}.txt")
        else:
            list_number = len(text_files) + 1
            shopping_list_name = f"shoppinglist{list_number}"
            file_path = os.path.join(directory_path, f"{shopping_list_name}.txt")

    elif choice == '3':
        print("Existing text files:")
        for i, text_file in enumerate(text_files, start=1):
            print(f"{i}. {text_file}")

        list_choice = int(input("Enter the number of the list you want to delete and create a new one: ")) - 1
        file_to_delete = os.path.join(directory_path, text_files[list_choice])
        os.remove(file_to_delete)
        print(f"{text_files[list_choice]} deleted.")

        custom_name_choice = input("Do you want to enter a custom name for the new list? (yes/no): ").lower()

        if custom_name_choice == 'yes':
            shopping_list_name = input("Enter a name for the new shopping list: ")
            file_path = os.path.join(directory_path, f"{shopping_list_name}.txt")
        else:
            list_number = len(text_files) + 1
            shopping_list_name = f"shoppinglist{list_number}"
            file_path = os.path.join(directory_path, f"{shopping_list_name}.txt")

    else:
        print("Invalid choice. Exiting.")
        return

    while True:
        item = input("Enter an item to add to your shopping list (press Enter to finish, type '%%**' to exit): ")

        if not item:
            break

        if item == "%%**": # Word to end list
            break

        shopping_list.append(item)

    with open(file_path, "w") as file:
        for item in shopping_list:
            file.write(f"{item}\n")

    print(f"Shopping list created successfully! Check '{file_path}'.")

if __name__ == "__main__":
    create_shopping_list()
