class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def __str__(self):
        return f"Employee(Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Gender: {self.gender})"


# Sample usage
if __name__ == "__main__":
    emp = Employee("Alice", 30, 50000, "Female")
    print(emp)
