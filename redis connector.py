import redis
import time
from redistimeseries.client import Client

import datetime

r = redis.Redis(
    host= "127.0.0.1",
    port= "6379")


class BloodPressureReading:
    def __init__(self, min_bp, max_bp):
        self.time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
        self.min_bp = min_bp
        self.max_bp = max_bp

class sp02Reading:
    def __init__(self, o2):
        self.time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
        self.oxygen = o2

class pulseReading:
    def __init__(self, heartbeat):
        self.time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
        self.heartbeat = heartbeat



class Patient:
    def __init__(self, name):
        self.name = name
        self.id = "autogenerateID"
        self.bp = []
        self.sp02 = []
        self.pulse = []

    def receive_vitals(self, bp_reading, sp_reading, pulse_reading):
        self.bp.append(bp_reading)
        self.sp02.append(sp_reading)
        self.pulse.append(pulse_reading)
        print("vitals updated")

    def get_cur_vitals(self):
        print("BLOOD PRESSURE: ", self.bp[-1].min_bp, self.bp[-1].max_bp)
        print("SP02: ", self.sp02[-1])
        print("PULSE: ", self.pulse[-1])

    def see_all_bp(self):
        for element in self.bp:
            print(element.min_bp, element.max_bp)   


# p = Patient("Boris")
# p.receive_vitals(bp_sample_1, 98, 100)
# p.get_cur_vitals()
# print("Second Iteration")
# p.receive_vitals(bp_sample_2, 87, 120)



#from here on, experiments
rts = Client()


def delete_previous():
    rts.delete("blood_min")
    rts.delete("blood_max")
    rts.delete("sp02")
    rts.delete("pulse")
    print("all previous databases deleted")

def create_all_series():
    rts.create('blood_min', labels={'Time':'Series'})
    rts.create('blood_max', labels={'Time':'Series'})
    rts.create('sp02', labels={'Time':'Series'})
    rts.create('pulse', labels={'Time':'Series'})
    print("Timeseries created")

def add_blood_samples():
    bp_sample_1 = BloodPressureReading(50, 120)
    time.sleep(1)
    bp_sample_2 = BloodPressureReading(60, 110)
    time.sleep(1)
    bp_sample_3 = BloodPressureReading(70, 130)

    rts.add("blood_min", bp_sample_1.time, bp_sample_1.min_bp)
    rts.add('blood_min', bp_sample_2.time, bp_sample_2.min_bp)
    rts.add("blood_min", bp_sample_3.time, bp_sample_3.min_bp)
    #print(rts.get("blood_min"))


    rts.add("blood_max", bp_sample_1.time, bp_sample_1.max_bp)
    rts.add('blood_max', bp_sample_2.time, bp_sample_2.max_bp)
    rts.add("blood_max", bp_sample_3.time, bp_sample_3.max_bp)
    #print(rts.get("blood_max"))

def add_sp02_samples():
    o2_sample_1 = sp02Reading(98)
    time.sleep(1)
    o2_sample_2 = sp02Reading(70)
    time.sleep(1)
    o2_sample_3 = sp02Reading(97)
    rts.add("sp02", o2_sample_1.time, o2_sample_1.oxygen)
    rts.add("sp02", o2_sample_2.time, o2_sample_2.oxygen)
    rts.add("sp02", o2_sample_3.time, o2_sample_3.oxygen)

def add_pulse_samples():
    pulse_sample_1 = pulseReading(98)
    time.sleep(1)
    pulse_sample_2 = pulseReading(54)
    time.sleep(1)
    pulse_sample_3 = pulseReading(120)
    rts.add("pulse", pulse_sample_1.time, pulse_sample_1.heartbeat)
    rts.add("pulse", pulse_sample_2.time, pulse_sample_2.heartbeat)
    rts.add("pulse", pulse_sample_3.time, pulse_sample_3.heartbeat)

delete_previous()
create_all_series()
add_blood_samples()
add_sp02_samples()
add_pulse_samples()
