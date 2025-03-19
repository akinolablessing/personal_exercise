from human import Human


class Employee(Human):
    def __init__(self, employee_id, name, salary, date_of_birth: str, gender, height):
        super().__init__(name, date_of_birth, gender, height)
        
