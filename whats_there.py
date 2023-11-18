import os


def list_tkinter_programs():
    programs = []
    folder_path = "C:\\Users\\haris"

    # Scan the folder for Python files
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            program_name = filename[:-3]
            programs.append(program_name)

    # Display the programs with serial numbers
    for i, program in enumerate(programs, start=1):
        print(f"{i}. {program}")

    return programs


def run_tkinter_program(programs, serial_number):
    try:
        selected_program = programs[serial_number - 1]
        program_path = f"C:/Users/haris/{selected_program}.py"  # Replace with the actual program path
        os.system(f"python {program_path}")
    except IndexError:
        print("Invalid serial number. Please try again.")


# Main program
programs = list_tkinter_programs()
selected_serial = int(input("Enter the serial number of the program you want to run: "))
run_tkinter_program(programs, selected_serial)
