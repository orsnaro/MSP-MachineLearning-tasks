from spr import *

   #----------------------------------------CHILD CLASSES -----------------------------------------#
#prof rank: teach asis , lecturer , asis.prof ,  associate.prof , prof 
#salary :  i know we all want to know :) #speciality #courses he teach 
class Prof ( Person ) : 
   def __init__(self, id: str, name: str, age: int, is_prof: bool, speciality: str , rank : int , salary : float) -> None:
      super().__init__(id, name, age, is_prof, speciality)
      self.rank = rank
      self.salary = salary
      self.save_id()

      def save_id(self) : 
         Person.ids_prof.append([self.id] = [f"name : {self.name}" , f"age : {self.age}" , f"Previlage : {'Professor' if self.is_prof == True else 'Student' }" , f"Department : {self.speciality}" , f"Academic Rank : {self.rank}" , f"Salary : {self.salary}"  ] )


class Student ( Person ) :  #study_year  #current_GPA  #fees_must_pay
   def __init__(self, id: str, name: str, age: int, is_prof: bool, speciality: str , year : int ,  GPA : float ) -> None:
      super().__init__(id, name, age, is_prof, speciality)
      self.year = year
      self.GPA = GPA

      def save_id(self) : 
          Person.ids_student.append([self.id] = [f"name : {self.name}" , f"age : {self.age}" , f"Previlage : {'Professor' if self.is_prof == True else 'Student' }" , f"Department : {self.speciality}" , f"Study Year : {self.year}" , f"Current GPA : {self.GPA}"  ] ) 




class Lab (Building) : ...  #TODO #main_tools  #speciality 
class hall (Building) : ...  #TODO #shedule of profs name and time they come  #hell : type events hall or course lecture hall?
    

# CHILDS OF SPECIALITY ( TODO soon )
class Mech (Speciality) : ... #mech course list
class Elec (Speciality) : ...#Elec course list


