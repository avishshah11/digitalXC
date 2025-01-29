import pandas as pd
from employee import Employee

class FileHandler:
    def read_employee_data(file_path, sheet_name):
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        return [Employee(row['Employee_Name'], row['Employee_EmailID']) for _, row in data.iterrows()]
    
    def read_last_year_data(file_path, sheet_name):
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        return [{'Employee_Name': row['Employee_Name'], 'Secret_Child_Name': row['Secret_Child_Name']} for _, row in data.iterrows()]
    
    def save_secret_santa_assignments(file_path, assignments):
        df = pd.DataFrame(assignments)
        df.to_csv(file_path, index=False)
