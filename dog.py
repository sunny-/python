class Dog:

    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText

    def speak(self):
        return self.speakText

    def getName(self):
        return self.name

    def birthDate(self):
        return (str(self.month) + '/' + str(self.day) + '/' + str(self.year))

    def changeBark(self,new_bark):
        self.speakText = new_bark
        return self.speakText

    def __add__(self,otherDog):
        return Dog("Puppy of " + self.name + " and " + otherDog.name, \
                   self.month, self.day, self.year + 1, \
                   self.speakText + otherDog.speakText)
  
def main():      
    boyDog = Dog("Mesa", 5, 15, 2004, "WOOOOF")
    girlDog = Dog("Sequoia", 5, 6, 2004, "barkbark")
    print(boyDog.speak())
    print(girlDog.speak())
    print(boyDog.birthDate())
    print(girlDog.birthDate())
    boyDog.changeBark("woofywoofy")
    print(boyDog.speak())
    puppy = boyDog + girlDog
    print (puppy.speakText)
    print(puppy.speak())
    print(puppy.getName())
    print(puppy.birthDate())

    
