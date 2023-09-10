word = "[name]"

with open("/Users/umakantmanore/Desktop/amu/practice/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("/Users/umakantmanore/Desktop/amu/practice/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        replaced_letter = letter.replace(word, stripped_name)
        with open(f"/Users/umakantmanore/Desktop/amu/practice/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode = 'w') as new_letter:
            new_letter.write(replaced_letter)
