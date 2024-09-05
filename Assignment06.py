# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using classes and methods
# with the seperation of concerns design principle
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Ogonna Anunoby, 09/04/2024, First attempt at Assignment 06
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer methods that work with Json files

    ChangeLog: (Who, When, What)
    Ogonna Anunoby, 09/04/2024, created the class and wrote methods to read from and write to the Json file
    """

    # When the program starts, read the file data into table
    # Extract the data from the file
    # Read from the Json file
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list) -> list:
        """
        A method to read student registraion data from a Json file and store it into a list.

        ChangeLog: (Who, When, What)
        Ogonna Anunoby, 09/04/2024, Created method
        
        :param file_name: string containing the name of the file
        :param student_data: list for holding student registration information
        :return student_data: list containing student registration information stored in the Json file
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e: # Catch FileNotFound exception
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e: # Catch general exception
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list) -> None:
        """
        A method to write and save student registration data to a Json file.

        ChangeLog: (Who, When, What)
        Ogonna Anunoby, 09/04/2024, Created method
        
        :param file_name: string data holding the name of the file
        :param student_data: list data used to hold student registration information
        :return None: No data returned
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The Json file has the following registration data saved:")
            for student in student_data:
                print(f"You have registered {student["FirstName"]} {student["LastName"]} for {student["CourseName"]}.")
        except TypeError as e: # Catch TypeError exception
            IO.output_error_messages("Please check that the data is a valid JSON format.", e)
        except Exception as e: # Catch general exception
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer methods that manage user input and output

    ChangeLog: (Who, When, What)
    Ogonna Anunoby, 09/04/2024, Created the class and added methods for input, output, data display, and displaying custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None) -> None:
        """ This method displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        Ogonna Anunoby, 09/02/2024, Created method

        :param menu: string containing user menu
        :param error: exception object for the error
        :return None: No data returned
        """
        print(message, end="\n\n")
        if error is not None: # prints error information if error object is passed
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str) -> None:
        """ This method displays the a menu of choices to the user

        ChangeLog: (Who, When, What)
        Ogonna Anunoby, 09/02/2024, Created method
        
        :param menu: string containing user menu
        :return None: No data returned
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.


    @staticmethod
    def input_menu_choice() -> str:
        """ This method gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Ogonna Anunoby, 09/02/2024, Created function

        :param None: No parameters
        :return choice: string with user's menu choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice


    @staticmethod
    def output_student_courses(student_data: list) -> None:
        """ This method displays the class each student registered for to the user

        ChangeLog: (Who, When, What)
        Ogonna Anunoby, 09/02/2024, Created method

        :param student_data: list containing student registration information
        :return None: No data returned
        """
        
        # Process the data to create to display current student registration data
        print()
        print("-" * 50)
        for student in student_data:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-" * 50)
        print()
    

    @staticmethod
    def input_student_data(student_data: list) -> list:
        
        """ This method gets the student's first name, last name, course they want to register for from the user

        ChangeLog: (Who, When, What)
        Ogonna Anunoby, 09/04/2024, Created method

        :param student_data: list containing student registration information
        :return student_data: list containing updated student registration information
        """
        
        try:
            # Input the data
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha(): # Check if only letters are entered
                raise ValueError("The first name should only contain letters.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha(): # Check if only letters are entered
                raise ValueError("The last name should only contain letters.")
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        else:
            course_name = input("Enter the name of the course: ")
            student = {"FirstName": student_first_name,"LastName": student_last_name, "CourseName" : course_name}
            student_data.append(student) # Load student dicitionary into our collection (list of dictionaries)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        return student_data


# End of function definitons



# Beginning of the main body of this script

# When the program starts, read the file data into table
# Extract the data from the Json file into a list of dictionaries
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks to present and process the data
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Get new data (and display the change)
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":  # Display current data 
        IO.output_student_courses(student_data=students)  # Added this to improve user experience
        continue

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop

print("Program Ended")
