class Person:
  name = ""

  def __init__(self, name, internationalId):
   self.name = name
   self.internationalId = internationalId
  def getInfo(self):
    print("this person's name is  " + self.name + " and international id is " + self.internationalId)

class Student(Person):
   def __init__(self, name, internationalId, studentId):
    super().__init__(name, internationalId)
    self.studentId = studentId
      
   def getInfo(self):
     print("this student's name is " + self.name + " and id is " + self.studentId + " and international id is " + self.internationalId)
      
   def study(self, subject):
      print(self.name + " is studying " + subject)

class Doctor(Person):
   def __init__(self, name, internationalId, doctorId):
    super().__init__(name, internationalId)
    self.doctorId = doctorId
      
   def getInfo(self):
     print("this doctor's name is " + self.name + " and id is " + self.doctorId + " and international id is " + self.internationalId)
      
   def treat(self, patient):
      print(self.name + " is treating " + patient)
   def diagnose(self, patient):
      print(self.name + " is diagnosing " + patient)


p1 = Person("John", "123456")
p1.getInfo()
p2 = Student("Jane","30380310", "A0123456")
p2.getInfo()
p2.study("Math")
p3 = Doctor("Mary", "12345678", "D0123456")
p3.getInfo()
p3.treat("John")
p3.diagnose("Jane")