# ==========================================
# MINI PROJECT: EMPLOYEE PAYROLL SYSTEM
# ==========================================
# --------------------------------------

# ==========================================
# Step 1: Global Variable
# ==========================================

bonus_percentage = 12
# --------------------------------------

# ==========================================
# Step 2: Create Employee Class
# ==========================================

class Employee:

    # Class Variable

    company_name = "InfotechLabs"


    # Constructor

    def __init__(self, name, salary, currency):

        # Public Variable

        self.name = name

        # Private Variable

        self.__salary = salary

        # Protected Variable

        self._currency = currency

    # ======================================
    # Public Method
    # ======================================

    def show_details(self):

        print("Employee Name:", self.name)

        print("Company:", Employee.company_name)

        print("Currency:", self._currency)


    # Private Method

    def __calculate_bonus(self):

        bonus = (self.__salary * bonus_percentage) / 100

        return bonus


    # Protected Method

    def _convert_currency(self):

        print("Currency conversion happening")


    # Public Method

    def generate_salary(self):

        # Call protected method

        self._convert_currency()

        # Call private method

        bonus = self.__calculate_bonus()

        # Local Variable

        final_salary = self.__salary + bonus

        print(
            "Final Salary:",
            final_salary,
            self._currency
        )
# --------------------------------------

# ==========================================
# Step 4: Inheritance
# ==========================================

class Manager(Employee):

    # Method Overriding

    def show_details(self):

        # Parent Method Call

        super().show_details()

        print("Role: Manager")
# --------------------------------------

# ==========================================
# Step 5: Object Creation
# ==========================================

e1 = Employee("Shivam", 50000, "INR")

e2 = Manager("Rahul", 80000, "USD")


e1.show_details()

e1.generate_salary()

e2.show_details()

e2.generate_salary()

# --------------------------------------

# ==========================================
# Step 6: Testing
# ==========================================

# Public Variable
# Should work

print(e1.name)


# Protected Variable
# Works but not recommended

print(e1._currency)


# Private Variable
# Will fail

# print(e1.__salary)

# Output:
# AttributeError


# Name Mangling

print(e1._Employee__salary)
# --------------------------------------

# ==========================================
# BONUS CHALLENGE
# Setter Method + Validation
# ==========================================

class Employee2:

    company_name = "InfotechLabs"

    def __init__(self, name, salary, currency):

        self.name = name

        self.__salary = salary
        
        self._currency = currency


    def set_salary(self, new_salary):

        if new_salary < 0:

            print("Salary cannot be negative")

        else:

            self.__salary = new_salary

            print("Salary updated")


    def show_salary(self):

        print("Salary:", self.__salary)


emp = Employee2("Aman", 40000, "INR")

emp.show_salary()

emp.set_salary(60000)

emp.show_salary()

emp.set_salary(-100)

# ==========================================
# OUTPUT EXAMPLE
# ==========================================

# Employee Name: Shivam
# Company: InfotechLabs
# Currency: INR
# Currency conversion happening
# Final Salary: 56000.0 INR

# Employee Name: Rahul
# Company: InfotechLabs
# Currency: USD
# Role: Manager
# Currency conversion happening
# Final Salary: 89600.0 USD

# ==========================================
# IMPORTANT CONCEPTS LEARNED
# ==========================================

# Global Variable
# Shared globally

# Class Variable
# Shared by all objects

# Instance Variable
# Separate for every object

# Public Variable
# Accessible everywhere

# Protected Variable (_variable)
# Convention only
# Accessible but not recommended

# Private Variable (__variable)
# Hidden using name mangling

# Local Variable
# Method level operation