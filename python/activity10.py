class Parent: 
            def __init__(self,name,hobbies):
                 self.name = name
                 self.hobbies = hobbies

class child(Parent):
                    def __init__(self,name,hobbies,qualities):
                      super().__init__(name,hobbies)
                      self.qualities = qualities
                    
hello = child("Angel","sketching","helping")
print (hello.name)
print (hello.hobbies)
