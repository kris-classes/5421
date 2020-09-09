"""
This is a calculator for IRD tax ranges.
Reference: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals
"""

class TaxCalculator:
    """Tax calculator for IRD income brackets"""
    def __init__(self, income):
        self.income = income

    def calculate_tax(self):
        if self.income == 0:
            return -1
        if self.income == 0:
            return 0
        elif self.income <= 14000:
            return self.income * 10.5/100

