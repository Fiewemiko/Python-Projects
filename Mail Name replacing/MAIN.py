PLACEHODLER = "Guys"

with open("./my_file.txt", mode="r") as file:
    list_of_names = file.readlines()

with open("Letter.txt","r") as letter:
    letter_content = letter.read()
    for name in list_of_names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHODLER, stripped_name)
        with open(f"./Ready to send/letter_for_{stripped_name}", mode="w") as completed_letter:
            completed_letter.write(new_letter)



