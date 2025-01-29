import random

class SecretSanta:
    def __init__(self, employees, last_year_pairs):
        self.employees = employees
        self.last_year_pairs = last_year_pairs
        self.last_year_lookup = {pair['Employee_Name']: pair['Secret_Child_Name'] for pair in last_year_pairs}
        print(self.last_year_lookup)
    
    def generate_pairs(self):
        shuffled_employees = self.employees.copy()
        random.shuffle(shuffled_employees)
        
        assignments = []
        
        for employee in self.employees:
            available_choices = [e for e in shuffled_employees if e.name != employee.name
                                 and e.name != self.last_year_lookup.get(employee.name)]
            
            if not available_choices:
                raise ValueError("Unable to assign a unique secret child for each employee.")
            
            secret_child = available_choices.pop(0)
            shuffled_employees.remove(secret_child)
            
            assignments.append({
                'Employee_Name': employee.name,
                'Employee_EmailID': employee.email,
                'Secret_Child_Name': secret_child.name,
                'Secret_Child_EmailID': secret_child.email
            })
        
        return assignments
