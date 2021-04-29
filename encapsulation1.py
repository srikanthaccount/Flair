# Python program to
# demonstrate protected members
 
 
# Creating a base class

#Single Level inheritance
class employee():
    _full_name='Sungard'
    def __init__(self):
        print("Employee class")
    def e_name(self):
        return self._full_name

class student(employee):
    def student_name(self,s_name):
        self.s_name=s_name
    def recruted(self):
         print("{} is recruted for {}".format(self.s_name,self.e_name()))

obj=student()

obj.student_name("suresh")
obj.recruted()

employee._full_name="Flair Tech"
obj.student_name("Ramesh")
obj.recruted()

obj._full_name="Tech mahendra"
obj.student_name("HArish")
obj.recruted()

print(employee._full_name)

print('#####################')
# multiple inheritance

class employee():
    fname="Technologies"
    def __init__(self):
        print("Employee class")
    def e_name(self,full_name):
        self.ename=full_name
        
class pg_class():
    def sem(self,sem_name):
        self.sem_name = sem_name


class student(employee,pg_class):
    def student_name(self,s_name):
        self.s_name=s_name
    def recruted(self):
         print("{} is recruted for {}".format(self.s_name,self.ename))
    def get_sem(self):
        print(self.sem_name)

obj=student()
obj.e_name("Flair")
obj.student_name("suresh")
obj.recruted()

obj=student()
obj.e_name("sungard")
obj.student_name("Srikanth")
obj.recruted()

obj.sem("first sem")
obj.get_sem()

class Maths():
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        print(self.first+self.second)

    def sub(self):
        print(self.first-self.second)
    
    def multip(self):
        print(self.first*self.second)

obj= Maths(10,20)

obj.add()



class Fibn():
    first = 0
    second = 1
    def __init__(self):
        print("Fib seriess")

    def fib(self,num):
        result=[]
        result.append(self.first)
        temp=self.second
        while temp<num:
            #import pdb;pdb.set_trace()
            result.append(temp)
            temp=self.first+self.second
            self.first= self.second
            self.second = temp
            
        return result
        

obj = Fibn()

res= obj.fib(10)



















    


































