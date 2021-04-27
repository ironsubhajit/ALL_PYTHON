class Dog():
    """A simple attempt to model a Dog."""

    def __init__(self,name,age):
        """initialize name and age attribute."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name.title()} rolled over!")


my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()
print(f"{my_dog.name} is {my_dog.age} years old.")