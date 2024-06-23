import os

def main():
    folder_name = "Sparx math"
    pfp_file = os.path.join(folder_name, "bookmark.txt")

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    counter = 1
    letter_counter = ord('a')
    skipped_sequence = None

    while True:
        if skipped_sequence is not None:
            user_input = input(f"Skipping {skipped_sequence}. Type %%* {skipped_sequence} to fill it in: ")
            if user_input.startswith(f"%%* {skipped_sequence}"):
                with open(pfp_file, "a") as file:
                    file.write(f"{counter}{chr(letter_counter)} {skipped_sequence}\n")
                    letter_counter += 1
                    skipped_sequence = None
        else:
            user_input = input(f"{counter}{chr(letter_counter)} ")

        if user_input.lower() == "%%**":
            counter += 1
            letter_counter = ord('a')
            skipped_sequence = None
        elif user_input.lower().startswith("%%*"):
            skipped_sequence = user_input.split(maxsplit=1)[1]
        elif user_input.lower().startswith("%%%"):
            try:
                sequence = user_input.split(maxsplit=1)[1]
                with open(pfp_file, "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        if line.startswith(f"{sequence}"):
                            print(f"Content for {sequence}: {line.split(maxsplit=1)[1]}")
            except IndexError:
                pass
        else:
            with open(pfp_file, "a") as file:
                file.write(f"{counter}{chr(letter_counter)} {user_input}\n")
                letter_counter += 1

if __name__ == "__main__":
    main()
