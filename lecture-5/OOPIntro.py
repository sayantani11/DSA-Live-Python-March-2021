class Human:

    def __init__(self, name="Any"):
        self.name = name

    def sayHello(self):
        print("Hello from " + self.name)

anuj = Human("Anuj Garg")

Human.sayHello(anuj)

anuj.sayHello()

# anuj.sayHello()
#
# ravi = Human()
#
# ravi.sayHello()