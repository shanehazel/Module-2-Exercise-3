# pseudocode

# make a method
def process ():

    # open a text file for writing
    with open("mylife.txt", "w") as output_file:

        # make a loop for the inputting of lines
        while True:

            # ask user for a line
            input_user = input("Enter line: ")
            output_file.write(input_user + "\n")

            # ask the user if there are more lines to add
            input_user1 = input ("Are there more lines y/n? ")
            
            # if the user is done with their lines, break the loop
# end of method
process ()