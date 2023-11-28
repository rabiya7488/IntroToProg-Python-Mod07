# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This Assignment Demonstrates classes and objects
# Change Log: (Who, When, What)
#   Rabiya Wasiq,11/26/2023,Created Script
#   Rabiya Wasiq 11/27/2023, Updated comments
# ------------------------------------------------------------------------------------------ #



import json
from json import JSONDecodeError
from typing import TextIO

#------------Data classes--------------
class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The student's first name.
    - last_name (str): The student's last name.

    ChangeLog:
    - Rabiya Wasiq, 11.26.2030: Created the class.
    """

    def __init__(self, first_name: str = '', last_name: str = ''):
        self.__first_name = first_name
        self.__last_name = last_name

    @property  # (Use this decorator for the getter or accessor)
    def first_name(self):
        return self.__first_name.capitalize()  # formatting code

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        return self.__last_name.capitalize()  # formatting code

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        return f'{self.first_name},{self.last_name}'


class Student(Person):
    """
    A sub-class of Person
    A class representing student data.

    Properties:
    - first_name (str): The student's first name.
    - last_name (str): The student's last name.
    - course_name: The course registered for by the student.

    ChangeLog:
    - Rabiya Wasiq, 11.26.2030: Created the class.
    """

    def __init__(self, first_name: str = '', last_name: str = '', course_name : str = ''):
        super().__init__(first_name=first_name, last_name=last_name)
        self.__course_name = course_name

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, value: str):
        self.__course_name = value
    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.course_name} '

#--------------Processing-----------------

class FileProcessor:
    """
    A collection of processing layer functions that read and write data from file
    Rabiya Wasiq, Created class, 11/19/23
    """

    @staticmethod
    def read_data_from_file(File_Name: str, student_data: list[Student]) -> list[Student]:
        """
        This function reads data from Json file and stores it into a list of dictionaries
        :param File_Name:
        :return: list[dict[str.str,str]]
            Rabiya Wasiq, 11/19/23, Created Function
        """
        File_Name : str
        list_of_dictionary_data : list[dict[str,str,str]] = []
        file :TextIO = None
        try:
            file = open(File_Name, 'r')
            list_of_dictionary_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_message('Json file not found, creating it...',e)
            file = open(File_Name, 'w')
        except JSONDecodeError as e:
            IO.output_error_message('Json file does not contain any data, resetting it..',e)
            file = open(File_Name, 'w')
            json.dump(list_of_dictionary_data, file)
        except Exception as e:
            IO.output_error_message('Unexpected Technical error',e)
        finally:
            if not file.closed:
                file.close()
        for student in list_of_dictionary_data:
            student_object: Student = Student(first_name=student["First_Name"],
                                          last_name=student["Last_Name"],
                                          course_name=student["Course_Name"])
            student_data.append(student_object)
        return student_data

    @staticmethod
    def writing_data_to_file(new_student: Student, student_data:list[Student], File_Name: str ):
        """
        Writes data to Json file in the format list of dictionaries.
        :param student_row:
        :param students_data:
        :return:None
                Rabiya Wasiq, 11/19/23, Created Function
        """
        student_data: list[Student]
        File_Name: str
        file: TextIO = None
        list_of_dictionary_data: list[dict] = []
        new_student: Student

        if new_student.first_name == '' or new_student.last_name == '' or new_student.course_name == '':
            IO.output_message('Please enter student details')

        else:
            for student in student_data:
                student_json = {"First_Name": student.first_name, "Last_Name": student.last_name, "Course_Name": student.course_name}
                list_of_dictionary_data.append(student_json)

            try:
                file = open(File_Name, 'w')  # using the write function, to truncate the file
                json.dump(list_of_dictionary_data, file)
                file.close()
                IO.output_message('Student registration details recorded\n')
            except Exception as e:
                IO.output_error_message('Unexpected Technical error',e)
            finally:
                if not file.closed:
                    file.close()


#--------------Presenting----------------------
class IO:
    """
    A collection of presentation layer functions that manager user input and output
    Rabiya Wasiq, Created class, 11/19/23
    """

    @staticmethod
    def output_error_message(message : str, error:Exception=None):
        """ This function displays a custom error messages to the user
        default exception value set to none
          :return: None
                Rabiya Wasiq, 11/19/23, Created Function
        """
        print(message, end="\n\n")

        if error is not None:
            print("-- Technical Error Message -- ")
            print('-' * 50)
            print(error, error.__doc__, error.__str__(), type(error), sep='\n')


    @staticmethod
    def output_message(message : str):
        """ This function displays a custom messages to the user
          :return: None
                Rabiya Wasiq, 11/19/23, Created Function
        """
        print(message, end="\n\n")

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu options to the user
        :param menu:
        :return: None
                Rabiya Wasiq, 11/19/23, Created Function
        """
        print(menu)

    @staticmethod
    def input_menu_choice()->str:
        """
        This functions gets the menu choice from the user
        :return: str
                Rabiya Wasiq, 11/19/23, Created Function
        """
        menu_choice: str
        try:
            menu_choice = input("Enter your menu choice number: ")
            if menu_choice not in ("1", "2", "3", "4","5"):
                raise Exception("Please enter the correct menu choice")
        except Exception as e:
            IO.output_error_messages(e)
        return menu_choice

    @staticmethod
    def current_data_from_file(student_data:list[Student]) ->str:
        """
        This function displays all student data from the Json file, formatted in a string
        :param student_data:
        :return:str
                Rabiya Wasiq, 11/19/23, Created Function
        """
        student_data: list[Student]
        for student in student_data:
            IO.output_message(str(student))


    @staticmethod
    def input_student_data(student_data : list [Student]) -> Student:
        """
        This function gets first name, last name, course name from the user and adds them to a dictionary
        :param student_data:
        :return: Student
                Rabiya Wasiq, 11/19/23, Created Function
        """
        student_data: list[Student]
        student = Student()
        while True:
            try:
                student.first_name = input("What is the student's first name? ")
                break
            except ValueError:
                IO.output_error_message('Student First Name can only contain alphabetic characters')
                #Not passing error deatils
        while True:
            try:
                student.last_name = input("Enter the student's last name: ")
                break
            except ValueError:
                IO.output_message('Student Last Name can only contain alphabetic characters')

        student.course_name = input("Enter the course name: ")
        student_data.append(student)
        return student


    @staticmethod
    def present_student_data(new_student : Student):
        """
        This function presents data from a dictionary to the user in string formatting
        :param student_row:
        :return:None
                Rabiya Wasiq, 11/19/23, Created Function
        """
        new_student:Student
        if new_student.first_name == '' or new_student.last_name == '' or new_student.course_name == '':
            IO.output_message('Please enter student details again')
        else:
            message = f'{new_student.first_name} {new_student.last_name} has registered for {new_student.course_name}'
            IO.output_message(message)


    @staticmethod
    def exit_choice()->str:
        """
        This function presents the user the choice to exit the program
        :return:str
                Rabiya Wasiq, 11/19/23, Created Function
        """
        exit_choice: str = ''
        exit_choice = input("Do you wish to exit the program? Y/N").capitalize()
        return exit_choice


# Define the Data Constants
MENU: str = '''
----------------------------------------- 
---- Course Registration Program ----
  Select from the following menu:  
    1. View all students registered to date
    2. Register a New Student for a Course
    3. Show New student registration details  
    4. Save New student data to a file
    5. Exit the program

----------------------------------------- 
'''


# Define the Data Variables
FILENAME: str = 'Enrollments.json'
menu_choice: str = ''
new_student: Student = Student()
students: list[Student] = []




# Present and Process the data
while True:

    IO.output_menu(menu=MENU)  # Present Menu
    menu_choice = IO.input_menu_choice()

    # Menu choice 1 shows the data extracted from the JSON and saved in the two-dimensional list
    if menu_choice == '1':
        students = FileProcessor.read_data_from_file(File_Name=FILENAME,student_data=students)
        IO.current_data_from_file(student_data=students)

    # Getting student details from the user
    elif menu_choice =='2':
        new_student = IO.input_student_data(student_data=students) #New student object created

    #presenting new student registration details to the user
    elif menu_choice =='3':
        IO.present_student_data(new_student=new_student)

    #writing new student details to Json file
    elif menu_choice =='4':
        FileProcessor.writing_data_to_file(new_student =new_student,student_data=students,File_Name=FILENAME)

    #exiting the program
    elif menu_choice == '5':
        exit_choice = IO.exit_choice()
        if exit_choice == "Y":
            IO.output_message('\nPausing the program till you press Enter...\n')
            break
