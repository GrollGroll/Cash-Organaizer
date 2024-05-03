from datetime import datetime


date_str = input('Введите дату (ГГГГ-ММ-ДД): ')
date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

print(date_obj)
print(type(date_obj))