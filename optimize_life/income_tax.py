class IncomeTax:
    max_tax_cutoff = 550000  # top skatte grænse
    max_tax_level = 0.6  # top skat
    base_tax_level = 0.4  # basis skat
    tax_deduction_yearly = 40000  # bundfradrag
    labour_contribution = 0.08  # arbejdsmarkedsbidrag

    def __init__(self):
        """there is something here on how to pay income tax. change year, and also when """
        self.income_ytd = 0
        self.tax_deduction_extra = 0

    def add_tax_deduction(self, deduction: int):
        self.tax_deduction_extra += deduction

    def calculate_income_after_tax(self, income):
        income = income * (1 - self.labour_contribution)

        tax_deduction = self.tax_deduction_yearly + self.tax_deduction_extra
        income_above_tax_deduction = max(income - tax_deduction, 0)
        standard_taxable_income = min(self.max_tax_cutoff - tax_deduction, income_above_tax_deduction)
        standard_tax = standard_taxable_income * self.base_tax_level

        top_taxable_income = max(income - self.max_tax_cutoff, 0)
        top_tax = top_taxable_income * self.max_tax_level

        return income - standard_tax - top_tax

    def calculate_income_after_tax_monthly(self, income):
        return self.calculate_income_after_tax(income * 12) / 12

    def calculate_simple_income_tax_monthly(self, income):
        return income * 0.5
