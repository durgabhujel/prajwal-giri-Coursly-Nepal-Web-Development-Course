# def hello():
#     print('Hello')
#     print('World')
#     #return None

    
# r = hello()
# print(r)


# def bmw(self):
#     print(f'Hello, I am a {self}')

# bmw('bMW')

# a = 5  #a is the object of class int
# print(type(a))

# b = 'python'
# print(type(b))

# c = [1,2,3,4,5]
# print(type(c))





class students:
    def __init__(self,name,branch,languages,year,subjects):
        #instance attributes
        self.name=name
        self.branch=branch
        self.languages=languages
        self.year=year
        self.subjects=subjects
#instance methods
    def code(self):
        if self.branch == 'CSE' :
                def code_in_language(self,language):
                    print(f"{self.name} can code....")
                    print(f"{self.name} can code in {language}..")
        else:
            print(f"{self.name}, cannot code..")
    #def code_in_language(self,language):
       # print(f"{self.name} can code in {language}..")
    def information(self):
        information=f"name={self.name},branch={self.branch},languages={self.languages},year={self.year},subjects={self.subjects}"
        return information
s1=students("Manoj","CSE","Python","Third","Data Structure")
s2=students("Leo","Civil","None","Second","Thermo Dynamics")
s1.code()
#s1.code_in_language("Python")
s2.code()
s2.code_in_language("Python")
s1.information()