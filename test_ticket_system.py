import unittest
from ticket_queue import TicketQueue

class TestTicketSystem(unittest.TestCase):
    def test_generate_and_process_normal(self):
        queue = TicketQueue()
        queue.generate_tickets(3)
        self.assertEqual(len(queue.queue), 3)
        queue.process_tickets()
        self.assertEqual(len(queue.queue), 0)

    def test_zero_tickets(self):
        queue = TicketQueue()
        queue.generate_tickets(0)
        self.assertEqual(len(queue.queue), 0)

    def test_large_number_of_tickets(self):
        queue = TicketQueue()
        queue.generate_tickets(100)
        self.assertEqual(len(queue.queue), 100)

    def test_process_empty_queue(self):
        queue = TicketQueue()
        queue.process_tickets()  # should not raise error

if __name__ == '__main__':
    unittest.main()
