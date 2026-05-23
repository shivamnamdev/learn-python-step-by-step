# ==========================================
# MINI PROJECT: Banking System
# OOP + Inheritance
# ==========================================

# ==========================================
# Objective
# ==========================================

# Build a system where:
# = Different types of accounts exist
# = Each account behaves differently
# = Code is reused smartly
# ------------------------------------------

# ==========================================
# STEP 1: Base Class (Parent)
# All accounts share common features
# ==========================================

class BankAccount:

    def __init__(self, name, balance=0):

        self.name = name

        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

        print(
            f"{amount} deposited. "
            f"Balance: {self.balance}"
        )

    def show_balance(self):

        print(
            f"{self.name}'s Balance: "
            f"{self.balance}"
        )
# ------------------------------------------

# ==========================================
# STEP 2: Single Inheritance
# Savings Account inherits BankAccount
# ==========================================

class SavingsAccount(BankAccount):

    def add_interest(self):

        interest = self.balance * 0.05

        self.balance += interest

        print("Interest added:", interest)
# ------------------------------------------

# ==========================================
# STEP 3: Method Overriding
# Current Account overrides withdraw rule
# ==========================================

class CurrentAccount(BankAccount):

    def withdraw(self, amount):

        if self.balance - amount < -500:

            print("Overdraft limit exceeded!")

        else:

            self.balance -= amount

            print(
                f"{amount} withdrawn. "
                f"Balance: {self.balance}"
            )
# ------------------------------------------

# ==========================================
# STEP 4: Multilevel Inheritance
# Premium Savings → Extra benefits
# ==========================================

class PremiumSavings(SavingsAccount):

    def add_bonus(self):

        bonus = 100

        self.balance += bonus

        print("Bonus added:", bonus)
# ------------------------------------------

# ==========================================
# STEP 5: Hierarchical Inheritance
# Another branch from same parent
# ==========================================

class SalaryAccount(BankAccount):

    def credit_salary(self, amount):

        self.deposit(amount)

        print("Salary credited")
# ------------------------------------------

# ==========================================
# STEP 6: Multiple Inheritance
# Combine features
# ==========================================

class Loan:

    def take_loan(self, amount):

        print(f"Loan of {amount} approved")

class SmartAccount(SavingsAccount, Loan):

    def features(self):

        print(
            "Smart Account: "
            "Savings + Loan features"
        )
# ------------------------------------------

# ==========================================
# STEP 7: Testing (Main Program)
# ==========================================

# Savings Account

s = SavingsAccount("Shivam", 1000)

s.deposit(500)

s.add_interest()

s.show_balance()

print("-----------")


# Current Account

c = CurrentAccount("Rahul", 200)

c.withdraw(600)

print("-----------")


# Premium Savings (Multilevel)

p = PremiumSavings("Amit", 2000)

p.add_interest()

p.add_bonus()

p.show_balance()

print("-----------")


# Salary Account (Hierarchical)

sal = SalaryAccount("Neha", 0)

sal.credit_salary(30000)

sal.show_balance()

print("-----------")


# Multiple Inheritance

sm = SmartAccount("Priya", 5000)

sm.add_interest()

sm.take_loan(20000)

sm.features()
# ------------------------------------------

# ==========================================
# Concept Mapping
# ==========================================

# Single Inheritance
# = SavingsAccount

# Multilevel Inheritance
# = PremiumSavings

# Hierarchical Inheritance
# = SalaryAccount

# Multiple Inheritance
# = SmartAccount

# Method Overriding
# = CurrentAccount

# ==========================================
# REAL-WORLD UNDERSTANDING
# ==========================================

# = Banks don’t create everything
#   from scratch

# = They reuse base structure
#   and extend features

# ==========================================
# FINAL LEARNING
# ==========================================

# This is how real applications are built:
# not by writing new code every time,
# but by extending existing logic.

# ==========================================