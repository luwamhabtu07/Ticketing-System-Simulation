import time
import random
from collections import deque
from ticket import Ticket

class TicketQueue:
    def __init__(self):
        self.queue = deque()
        self.ticket_counter = 1

    def generate_tickets(self, num_tickets):
        for _ in range(num_tickets):
            ticket = Ticket(self.ticket_counter)
            self.queue.append(ticket)
            print(f"Generated: {ticket}")
            self.ticket_counter += 1
            time.sleep(random.uniform(0.2, 1.0))  # simulate random arrival times

    def process_tickets(self):
        while self.queue:
            ticket = self.queue.popleft()
            print(f"Serving: {ticket}")
            time.sleep(random.uniform(0.5, 1.5))  # simulate varying service time

