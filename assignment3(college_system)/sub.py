from spr import *

   #----------------------------------------CHILD CLASSES -----------------------------------------#
#prof rank: teach asis , lecturer , asis.prof ,  associate.prof , prof 
#salary :  i we all want to know :) #speciality #courses he teach 
class Prof ( Person ) : 
   def __init__(self, id: str, name: str, age: int, is_prof: bool, speciality: str , rank : int , salary : float) -> None:
      super().__init__(id, name, age, is_prof, speciality)
      self.rank = rank
      self.salary = salary

      def save_id(self , id) : 
         Person.ids_prof.append(id)


class Student ( Person ) :  #study_year  #current_GPA  #fees_must_pay
   def __init__(self, id: str, name: str, age: int, is_prof: bool, speciality: str , year : int ,  GPA : float ) -> None:
      super().__init__(id, name, age, is_prof, speciality)
      self.year = year
      self.GPA = GPA

      def save_id(self , id) : 
         Person.ids_student.append(id)




# class Lab (Building) : ...  #main_tools  #speciality 
# class hall (Building) : ...  #shedule of profs name and time they come  #hell : type events hall or course lecture hall?
    

# CHILDS OF SPECIALITY ( TODO soon )
# class Mech (Speciality) : ... #mech course list
# class Elec (Speciality) : ...#Elec course list


