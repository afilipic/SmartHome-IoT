
class Home(object):
    def __init__(self,pin):
        self.people_count = 0
        self.alarm = False
        self.alarm_pin = pin

    def more_people(self):
        self.people_count += 1

    def less_people(self):
        if (self.people_count > 0):
            self.people_count -= 1

    def set_alarm_true(self):
        self.alarm = True

    def set_alarm_false(self):
        self.alarm = False
