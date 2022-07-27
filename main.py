
class Employer:

    def __init__(self, first_name, last_name, age, job, salary, bonus):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.salary = salary
        self.bonus = bonus
        self.total_salary = self.salary

    def apply_bonus(self):
        self.total_salary = self.salary + self.bonus


class Department:

    user_list = []
    departments = []

    def __init__(self, name, first_name, last_name):
        super().__init__(first_name, last_name)
        self.name = name
        self.users = first_name + " " + last_name
        self.user_list.append(self.users)
        self.departments.append(self.name)

    @classmethod
    def num_users(cls):
        return len(cls.user_list)

    def display_employers(self):
        return self.user_list

    def display_departments(self):
        return self.departments






