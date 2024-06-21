#2. Python Programming Challenges for Customer Service Data Handling
#Objective: This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

#Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

#Problem Statement: Develop a program that:

#Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
#Implement functions to:
#Open a new service ticket.
#Update the status of an existing ticket  to "closed".
#Display all tickets.
#  (Bonus) filter by status

#Initialize with some sample tickets and include functionality for additional ticket entry.
#Example ticket structure:

#service_tickets = {
    #"Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    #"Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}}

service_tickets = {
        "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
        "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
    }

def open_ticket(ticket_id, customer, issue):
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}

def close_ticket(ticket_id):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = "closed"
    else:
        print("Ticket not found.")

def display_tickets():
    for ticket_id, ticket_info in service_tickets.items():
        print(f"Ticket ID: {ticket_id}")
        print(f"Customer: {ticket_info['Customer']}")
        print(f"Issue: {ticket_info['Issue']}")
        print(f"Status: {ticket_info['Status']}")
        print()


open_ticket("Ticket003", "Charlie", "Website down")
close_ticket("Ticket001")
display_tickets()
open_ticket("Ticket004", "Dave", "Billing inquiry")
display_tickets()

