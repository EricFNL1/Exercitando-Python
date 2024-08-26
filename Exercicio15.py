from datetime import datetime

birth_date = datetime(2003, 10, 23)

current_date = datetime.now()

# Calcule a diferença total em dias
difference_in_days = (current_date - birth_date).days

# Converta a diferença em anos, meses e dias
years = difference_in_days // 365
remaining_days = difference_in_days % 365
months = remaining_days // 30
days = remaining_days % 30

# Exiba a idade em anos, meses e dias
print(f"Idade: {years} anos, {months} meses e {days} dias")
