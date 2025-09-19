class Distance:
    UNITS = {
        "мм": 0.001,
        "см": 0.01,
        "м": 1,
        "км": 1000
    }

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_meters(self):
        return self.value * self.UNITS[self.unit]

    @classmethod
    def from_meters(cls, meters, unit):
        return cls(meters / cls.UNITS[unit], unit)

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_m = self.to_meters() + other.to_meters()
        return self.from_meters(total_m, self.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        result_m = self.to_meters() - other.to_meters()
        return self.from_meters(result_m, self.unit)
