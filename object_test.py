"""
    >>> test = Time(2, 15, 30)
    >>> test.convert_to_seconds()
    8130
"""
# Place your solution code on the line after this one...
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
def convert_to_seconds(t):
    minutes = t.hours * 60 + t.minutes
    seconds = minutes * 60 + t.seconds
    print(seconds)

if __name__ == '__main__':
    import doctest
    doctest.testmod()