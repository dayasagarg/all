from datetime import datetime, timedelta

curr = datetime.now()
curr_str = datetime.strftime(curr, "%Y-%m-%d")

prev_1 = curr - timedelta(days=1)
prev_2 = curr - timedelta(days=3)

pre_str_1 = datetime.strftime(prev_1, "%Y-%m-%d")
pre_str_2 = datetime.strftime(prev_2, "%Y-%m-%d")

pre_str_er = datetime.strftime(prev_1, "%d-%m-%Y")

print("pre_str_er::",pre_str_er)
