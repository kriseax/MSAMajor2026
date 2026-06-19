
class Student:
    def __init__(self, first_name, last_name, major, credit_hours, gpa, ID):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__ID = ID
        #self.__class_level = sel.
    
    def get_first_name(self) -> str:
        return self.__first_name
    
    def set_first_name(self, new_fname:str):
        self.__first_name = new_fname
        return

    def get_last_name(self) -> str:
        return self.__last_name
    
    def set_last_name(self, new_lname:str):
        self.__last_name = new_lname
        return

    def get_major(self) -> str:
        return self.__major
    
    def set_major(self, new_major:str):
        self.__major = new_major
        return

    def get_credit_hours(self) -> int:
        return self.__credit_hours

    def set_credit_hours(self, new_credits:int):
        self.__credit_hours = new_credits
        return
    
    def update_credit_hours(self, new_credits:int):
        self.__credit_hours += new_credits
        return
    
    def get_gpa(self)-> float:
        return self.__gpa
    
    def set_gpa(self, new_gpa:float):
        self.__gpa = new_gpa
        return
    
    def get_ID(self)-> str:
        return self.__ID

    def get_class_level(self)-> str:
        if self.__credit_hours > 90:
            return "Senior"
        elif self.__credit_hours > 60:
            return "Junior"
        elif self.__credit_hours > 30:
            return "Sophomore"
        else:
            return "Freshman"
    
    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}")
        print(f"Class Level: {self.get_class_level()}, Major: {self.__major}")
        print(f"GPA: {self.__gpa}, ID: {self.__ID}\n")
