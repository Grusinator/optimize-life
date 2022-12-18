class IncomeTax:
    max_tax_cutoff = 550000  # top skatte grænse
    max_tax_level = 0.6  # top skat
    base_tax_level = 0.4  # basis skat
    tax_deduction_yearly = 40000  # bundfradrag
    labour_contribution = 0.08  # arbejdsmarkedsbidrag

    def __init__(self):
        pass

    def calculate_income_tax(self, income):
        income = income * (1 - self.labour_contribution)

        income_above_tax_deduction = max(income - self.tax_deduction_yearly, 0)
        standard_taxable_income = min(self.max_tax_cutoff - self.tax_deduction_yearly, income_above_tax_deduction)
        standard_tax = standard_taxable_income * self.base_tax_level

        top_taxable_income = max(income - self.max_tax_cutoff, 0)
        top_tax = top_taxable_income * self.max_tax_level

        return income - standard_tax - top_tax

    def calculate_income_tax_monthly(self, income):
        return self.calculate_income_tax(income * 12) / 12
