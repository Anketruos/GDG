class Student():
    __grade = None
    def set_grade(self, grade):
        self.__grade = grade
    
    def get_grade(self):
        print(self.__grade)

s1 = Student()
s1.set_grade('A')
s1.get_grade()