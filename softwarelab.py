class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class EmployeeTable:
    def __init__(self):
        self.employee_data = []

    def add_employee(self, employee):
        self.employee_data.append(employee)

    def sort_table(self, sorting_parameter):
        if sorting_parameter == 1:
            self.employee_data.sort(key=self.compare_by_age)
        elif sorting_parameter == 2:
            self.employee_data.sort(key=self.compare_by_name)
        elif sorting_parameter == 3:
            self.employee_data.sort(key=self.compare_by_salary)
        else:
            print("Invalid sorting parameter. Please choose between 1, 2, or 3.")

    def compare_by_age(self, employee):
        return employee.age

    def compare_by_name(self, employee):
        return employee.name

    def compare_by_salary(self, employee):
        return employee.salary

    def print_table(self):
        print("Sorted Employee Data:")
        for employee in self.employee_data:
            print(employee)

table = EmployeeTable()

table.add_employee(Employee("161E90", "Raman", 41, 56000))
table.add_employee(Employee("161F91", "Himadri", 38, 67500))
table.add_employee(Employee("161F99", "Jaya", 51, 82100))
table.add_employee(Employee("171E20", "Tejas", 30, 55000))
table.add_employee(Employee("171G30", "Ajay", 45, 44000))

sorting_option = int(input("Enter the sorting number: "))
table.sort_table(sorting_option)
table.print_table()