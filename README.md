# Ticketing System Simulation

## 📌 Overview

This project simulates a ticketing system where customers take a number and wait for their turn to be served. It uses a queue data structure to manage the order of service.

---

## 🧱 Features

- Ticket class with ticket number and timestamp
- Queue for managing tickets
- Randomized timing for generation and service
- Separate phases for generation and processing
- Unit tests for normal and edge cases

---

## 📊 Flowchart

![Ticketing System Flowchart](diagrams/ticketing_system_flowchart.png)

---

## 🧪 Test Cases

We use `unittest` to validate:
- ✅ Normal case: 3-5 ticket flow
- ✅ Edge case: 0 tickets
- ✅ Edge case: very large number of tickets
- ✅ Edge case: negative input handled
- ✅ Edge case: string input handled

Run tests:
```bash
python -m unittest tests/test_ticket_system.py
