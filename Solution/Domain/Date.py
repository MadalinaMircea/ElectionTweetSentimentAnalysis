class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        day = str(self.day)
        if len(day) == 1:
            day = '0' + day
        return "{}-{}-{}".format(self.year, self.month, day)
