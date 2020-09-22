"""
This is a calculator for IRD tax ranges.
Reference: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals
"""

class TaxCalculator:
    """Tax calculator for IRD income brackets"""
    def __init__(self, income, country='nz'):
        self.income = income

    def calculate_tax(self):
        """Calculate the tax to pay"""
        if self.income == 0:
            return 0
        elif self.income <= 14000:
            return self.income * 10.5/100
        elif 14000 < self.income <= 48000:
            # Fix this
            first_bracket = 14000 * 10.5/100
            remaining_income = self.income - 14000
            second_bracket = 17.5/100 * remaining_income
            total_tax = first_bracket + second_bracket
            return total_tax
        elif 48000 < self.income <= 70000:
            return self.income * 30 / 100
        else:
            return self.income * 33 / 100

