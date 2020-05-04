import redis

def redisc():
    r = redis.Redis(
    host= "127.0.0.1",
    port= "6379")
    return r

r=redisc()
r.set("foo","bar")
r.get("foo")

class BloodPressureReading:
    def __init__(self, min_bp, max_bp):
        self.time = "a"#timestamp
        self.min_bp = min_bp
        self.max_bp = max_bp


bp_sample_1 = BloodPressureReading(60, 120)
bp_sample_2 = BloodPressureReading(50, 110)


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


p = Patient("Boris")
p.receive_vitals(bp_sample_1, 98, 100)
p.get_cur_vitals()
print("Second Iteration")
p.receive_vitals(bp_sample_2, 87, 120)


