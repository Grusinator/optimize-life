from dataclasses import dataclass


@dataclass
class EconomicStrategy:
    ensure_enough_money_on_private: bool = False
    loan_private_to_company: bool = True
    pay_off_loans: bool = True
    transfer_income_to_private: bool = True
    transfer_business_profit_to_capital: bool = True
    pay_back_private_loan: bool = False
