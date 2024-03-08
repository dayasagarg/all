

from datetime import datetime, timedelta

curr = datetime.now()
curr_str = datetime.strftime(curr, "%d-%m-%Y")
curr_str_emi = datetime.strftime(curr, "%d/%m/%Y")

print(curr_str)
print(curr_str_emi)




