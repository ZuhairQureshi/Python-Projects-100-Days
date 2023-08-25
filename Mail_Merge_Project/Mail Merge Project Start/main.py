#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# will contain names
Lines = []

# take all names (on different lines) and store separately into Lines array
with open("./Input/Names/invited_names.txt") as file:
    Lines = file.readlines()
    print(Lines)

# load the template into a string
with open("./Input/Letters/starting_letter.txt") as file:
    template = file.read()

previous_item = "[name]"

for i in range(len(Lines)):
    if "\n" in Lines[i]:
        Lines[i] = Lines[i][:-2]   # get rid of escape characters

    # make sure to replace the previous name in the template each time
    template = template.replace(previous_item, Lines[i])
    previous_item = Lines[i]

    # write the name into the template and then generate the file
    with open(f"./Output/ReadyToSend/letter_for_{Lines[i]}", mode="w") as f:
        f.write(template)


