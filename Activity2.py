import random
import time
def random_date(start,end):
    print(f"printing random date between{start} to {end}")
    random_generator=random.random()
    date_format="%m/%d/%Y"
    start_time=time.mktime(time.strptime(start,date_format))
    end_time=time.mktime(time.strptime(end,date_format))
    random_time=start_time+random_generator*(end_time-start_time)
    randomdate=time.strftime(date_format,time.localtime(random_time))
    return randomdate
print(random_date("11/3/2021","11/3/2022"))