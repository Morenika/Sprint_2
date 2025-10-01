# Задание 4

class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None and rest_days is not None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment


employee = EmployeeSalary.get_hours('Иван', None, 2, 'ivan@email.com')
employee = EmployeeSalary.get_email(employee.name, employee.hours, employee.rest_days, None)
print(employee.name, employee.hours, employee.email)
print('Зарплата за неделю:', employee.salary())
