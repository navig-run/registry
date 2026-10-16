# Transaction format: date,description,amount,category,account,notes
# Example:
# 2026-03-01,Payroll Direct Deposit,3500.00,income,checking,
# 2026-03-02,Whole Foods Market,-87.45,food,checking,Weekly groceries
# 2026-03-03,Electric Bill,-92.00,utilities,checking,
#
# RULES:
# - amount is positive for income, negative for expenses
# - category must be one of: income, housing, food, transport, utilities,
#   health, entertainment, clothing, education, savings, investments, taxes, miscellaneous
# - leave category blank if unknown — budget-analyst will categorize
