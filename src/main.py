from file_handler import FileHandler
from secret_santa import SecretSanta

def main():
    employees = FileHandler.read_employee_data('../assets/Employee-List.xlsx', sheet_name='Employee-List')
    last_year_pairs = FileHandler.read_last_year_data('../assets/Secret-Santa-Game-Result-2023.xlsx', sheet_name='Secret-Santa-Game-Result-2023')
    
    secret_santa = SecretSanta(employees, last_year_pairs)
    assignments = secret_santa.generate_pairs()
    
    FileHandler.save_secret_santa_assignments('../assets/Secret_Santa_Challenge.csv', assignments)

if __name__ == "__main__":
    main()
