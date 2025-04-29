from ticket_queue import TicketQueue

if __name__ == '__main__':
    system = TicketQueue()
    print("Generate tickets ....")
    system.generate_tickets(5)
    print("\nprocessing tickets ....")
    system.process_tickets()