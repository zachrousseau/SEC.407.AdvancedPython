# Program #01:

# Write a Python program that copies its own source code to a new file in the same folder, say “copy.py”.

# Console:
# Enter the Input File: Abuzneid.Assignment01.py
# Enger the Output File: copy.py
# <it will display the source code the screen and creates a new file “copy.py” identical to
# Abuzneid.Assignment01.py>

# Specifications
# • Create a function that opens both files and read from the first to the second.
# • Use write() and read() functions
# • After copy the source file to a copy file, print the copy file to the screen

# File name: Rousseau.Assignment.02.Program.01.py

def read_file(file_name):
    import os
    script_directory = os.path.dirname(os.path.abspath(__file__))

    file = open( ( script_directory + "\\" + file_name), "r", encoding='utf-8')

    return file.read()

def write_file(file_name, content):
    import os
    script_directory = os.path.dirname(os.path.abspath(__file__))

    with open(script_directory + "\\" + file_name, 'w', encoding='utf-8') as file:
        file.write(content)


def main():
    import os
    

    input_file = input("Enter the Input File")
    output_file = input("Enter the Output File")

    write_file(output_file, read_file(input_file))
    
    print(f"The file {output_file} has been created: \n\n" + read_file(output_file))


if __name__ == "__main__":
    main()