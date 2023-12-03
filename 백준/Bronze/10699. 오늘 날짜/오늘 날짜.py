from datetime import datetime

current_datetime = datetime.now()
formatted_date = current_datetime.strftime('%Y-%m-%d')
print(formatted_date)