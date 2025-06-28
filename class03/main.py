from abc import abstractmethod, ABC

# Encapsulation
class Hotel():
    def __init__(self, name, income):
        self.name = name
        self.__income = income # Private Attribute

    # Getter Functions
    def fetch_income(self):
        return self.__income

    # Setter Function
    def update_income(self, amount: int):
        # 100        +=  200
        self.__income += amount
        return self.__income


kababjees = Hotel('Kababjees', 100)
print(kababjees.name)
# print(kababjees.__income) # Error 
print(kababjees.fetch_income())

print(kababjees.update_income(200)) # 300
print(kababjees.update_income(700)) # 1000



# Abstraction
class Person(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_fine():
        pass


class Member(Person):
    def __init__(self):
        super().__init__()

    def calculate_fine(self, days):
        return days * 10
    
class Librarian(Person):
    def __init__(self):
        super().__init__()

    def calculate_fine(self, salary, days):
        return salary - days