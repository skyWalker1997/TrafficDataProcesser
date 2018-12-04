import re
def time_split(time):
    HH = re.split(':',time)[0]
    MM = int(re.split(':',time)[1])
    return HH,MM

def date_split(date):
    day = re.split(' ',date)[0]
    time = re.split(' ',date)[1]
    return day,time
