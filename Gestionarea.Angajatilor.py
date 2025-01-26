# Clasa de bază Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

# Subclasa Manager care moștenește Employee
class Manager(Employee):
    def __init__(self, name, salary, department):
        # Apelăm constructorul clasei părinte (Employee)
        super().__init__(name, salary)
        self.department = department

    # Suprascriem metoda get_details pentru Manager
    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"

# Creăm obiecte de tip Employee și Manager
emp = Employee("John", 3000)
mgr = Manager("Alice", 5000, "IT")

# Afișăm detaliile despre angajați
print(emp.get_details())  # "Employee: John, Salary: 3000"
print(mgr.get_details())  # "Manager: Alice, Salary: 5000, Department: IT"
