class Staff601():
    room = "304"

    def __init__(self,greeting):
        self.greeting = greeting

    def sayHi(self):
        print (self.greeting)


sunny = Staff601('hi')

uj = Staff601('hello')

sunny.sayHi()

uj.sayHi()

##sunny.room
##
##print (uj.room)
