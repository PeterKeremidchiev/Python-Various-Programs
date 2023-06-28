class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{'%02d' % self.hours}:{'%02d' % self.minutes}:{'%02d' % self.seconds}"

    def next_second(self):
        self.seconds += 1
        if self.hours + 1 > Time.max_hours:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        if self.minutes + 1 > Time.max_minutes:
            self.minutes = 0
            self.hours += 1
            self.seconds = 0
        if self.seconds + 1 > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
        return self.get_time()

t = Time(1, 20, 30)
print(t.next_second())
