#a module to send mock IOT requests every second

import requests, time, random

def random_bp():
    """Generate a random blood pressure range.
    Returns a dictionary with min and
    max blood pressure."""
    bp_min = random.randrange(60, 90)
    bp_max = random.randrange(100, 220)

    bp = [bp_min, bp_max]
    return bp

def random_sp02():
    """Generate a random SP02 value (oxygen)"""
    sp02 = random.randrange(60, 100)
    return sp02

def random_temp():
    temp = random.randrange(35, 42)
    return temp


def create_dict():
    """create a dictionary with all the random variables"""
    bp = random_bp()
    sp = random_sp02()
    temp = random_temp()
    vitals_dict = {"bp": bp, "sp": sp, "temp": temp}
    return vitals_dict

def push_data():
    """Push the data for one data point"""
    response = requests.post('http://127.0.0.1:5000/reception',
                         json=create_dict())
    return

while 1>0:
    push_data()
    time.sleep(0.3)
    

    
