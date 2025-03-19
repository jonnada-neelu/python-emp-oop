# Main file
from hr import ABC, abstractmethod


if __name__ == "__main__":
    emp1 = PermanentEmployees("101", "Amar", "IT", 70000, 3000)
    emp2 = ContractEmployees("A123", "Birav", "Sales_Manager", 70, 200)
    emp3 = Intern("F156", "Chirag", "Finance", 15000)
    
    employees = [emp1, emp2, emp3]
    
    for emp in employees:
        emp.display_details()
