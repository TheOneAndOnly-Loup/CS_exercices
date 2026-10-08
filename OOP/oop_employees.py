import random
class Employee:
    def __init__(self, id, name, job, salary, experience):
        self.id = id
        self.name = name
        self.job = job
        self.salary = salary
        self.experience = experience
        self.promotion = False
    def display(self):
        print(f"\nID: {self.id}, Name: {self.name}, Job position: {self.job}, Salary: {self.salary}, Experience: {self.experience}, Promoted?: {self.promotion}")
    def promote(self):
        if self.experience >= 5:
            self.salary *= 1.2
            self.promotion = True

class Ceo(Employee):
    def __init__(self, id, name, job, salary, experience, employees_managed, company_size):
        super().__init__(id, name, job, salary, experience)
        self.employees_managed = employees_managed
        self.company_size = company_size
    def display(self):
        super().display()
        print(f"Employees managed: {self.employees_managed}, Company size: {self.company_size}")


# employee1 = Employee(1, "John Doe", "Software Engineer", 75000, 3)
# employee2 = Employee(2, "Jane Smith", "Data Scientist", 85000, 7)

# employee1.promote()
# employee2.promote()

# employee1.display()
# employee2.display()

c = Ceo(random.randint(3, 10), "Jeff Bezos", "CEO", 150000, 10, 100, "Large")
c.display()
