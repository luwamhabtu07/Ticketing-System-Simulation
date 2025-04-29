import time
from datetime import datetime

class Ticket:
    def __init__(self, number):
        self.number = number
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Ticket # {self.number} | Time: {self.timestamp.strftime('%H:%M:%S')}"
    