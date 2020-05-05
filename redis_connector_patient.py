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

class SP02Reading:
    def __init__(self, o2):
        self.time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
        self.oxygen = o2

class PulseReading:
    def __init__(self, heartbeat):
        self.time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
        self.heartbeat = heartbeat

class TempReading:
    def __init__(self, temp):
        self.time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
        self.temp = temp



class Patient:
    def __init__(self, name):
        self.name = name
        self.id = "autogenerateID"
        self.rts = Client()
        self.delete_previous()
        self.create_all_series()

    def delete_previous(self):
        """delete any previously same name timeseries."""
        self.rts.delete("blood_min")
        self.rts.delete("blood_max")
        self.rts.delete("sp02")
        self.rts.delete("pulse")
        print("All previous timeseries deleted")

    def create_all_series(self):
        """Create all the time series that will contain all of the patients' data
        """
        self.rts.create('blood_min', labels={'Time': 'Series'})
        self.rts.create('blood_max', labels={'Time': 'Series'})
        self.rts.create('sp02', labels={'Time': 'Series'})
        self.rts.create('pulse', labels={'Time': 'Series'})
        print("Timeseries created")


    def add_blood_samples(self, blood_reading):
        """Convert a standard blood reading into a BloodPressureReading object and
        add it to both timeseries.
        """
        blood_reading = BloodPressureReading(blood_reading[0], blood_reading[1])
        self.rts.add("blood_min", blood_reading.time, blood_reading.min_bp)
        # print(rts.get("blood_min"))
        self.rts.add("blood_max", blood_reading.time, blood_reading.max_bp)
        # print(rts.get("blood_max"))

    def add_sp02_samples(self, sp02_reading):
        """Convert a standard SPO2 reading into a SP02Reading and add to its timeseries"""
        sp02_reading = SP02Reading(sp02_reading)
        self.rts.add("sp02", sp02_reading.time, sp02_reading.oxygen)

    def add_pulse_samples(self, pulse_reading):
        """Convert a standard pulse reading into a PulseReading and add to its timeseries"""
        pulse_reading = PulseReading(pulse_reading)
        self.rts.add("pulse", pulse_reading.time, pulse_reading.heartbeat)

    def add_temp_samples(self, temp_reading):
        """Convert a standard temperature (Celsius) into a TemperatureReading and add it to its timeseries"""
        temp_reading = TempReading(temp_reading)
        self.rts.add("temp", temp_reading.time, temp_reading.temp)


    def receive_vitals(self, bp_reading, sp_reading, pulse_reading):
        """Receive vitals from a push operation and add to the timeseries"""
        self.add_blood_samples(bp_reading)
        self.add_sp02_samples(sp_reading)
        self.add_pulse_samples(pulse_reading)
        print("vitals updated")


#p = Patient("Boris")
#p.receive_vitals([120, 60], 98, 100)
# time.sleep(2)
# p.receive_vitals([130, 90], 80, 170)



#from here on, experiments

# def get_all_ts(timeseries_name):
#     full_timeseries = rts.getrange(timeseries_name, 0, -1)
#     return full_timeseries
#
# print(get_all_ts("pulse"))
# pulse_sample_boris= pulseReading(98)
# r.hset("boris2", rts.create("borisblood", pulse_sample_boris.time, pulse_sample_boris.heartbeat))
# print(r.hget("boris2"))