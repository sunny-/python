class Person(object):
    def __init__(self, family_name, first_name):
        self.family_name = family_name
        self.first_name = first_name

    def __str__(self):
        return str(self.family_name) + str(self.first_name)


    def family(self):
        return self.family_name

    def first(self):
        return self.first_name

    def __cmp__(self,other):
        return cmp((self.family_name, self.first_name),(other.family_name, other.first_name))

    def say(self,other,something):
        return str(self.first_name) + ' says to ' + str(other.first_name) + ' '+something

    def sing(self,other,something):
        return self.say(other,something) + ' tra la la'
        


    
        
f = Person('ujs','Shanker')

g = Person('sunny','upa')

s = 'how u doing'

f.say(g,s)



class Calperson(Person):
    pass

##    def say(self,other,something):
##        return Person.say(self,other,'watsup!!! ' + something)



p1 = Calperson('tun','shank')













    

