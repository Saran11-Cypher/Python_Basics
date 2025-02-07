class Student:
    def __init__(self, Name, Tamil, English, Maths, Science, Social):
        self.Name = Name
        self.Tamil = Tamil
        self.English = English
        self.Maths = Maths
        self.Science = Science
        self.Social = Social
        self.total = Tamil + English + Maths + Science + Social

    def total_marks(self):
        print(f"{self.Name} scored a total of: {self.total}")
        
    def __del__(self):
        print("this is a destructor", self )
    
    def __str__(self):
        return(self.Name)
        
student1 = Student("King",90, 67, 100, 78, 98)
student2 = Student("Louis",56, 99, 80, 100, 88)
student3 = Student("Beckingham",97, 97, 100, 100, 98)
student4 = Student("Arthur",70, 77, 50, 88, 68)
student5 = Student("William",80, 97, 80, 100, 81)
student6 = Student("Alex",90, 100, 100, 68, 88)
student1.total_marks()
print(student1)
