from collections import deque
booking_stack = {}
application_queue = deque()
available_properties = ["land", "house", "vehicles", "furnitures"]

def book_property(user, property_name):
    if property_name in available_properties:
        available_properties.remove(property_name)
        booking_stack.setdefault(user, []).append(property_name)
        print(f"{user} booked {property_name}.")
    else:
        print(f"Sorry, {property_name} is not available.")

def undo_booking(user):
    if user in booking_stack and booking_stack[user]:
        last_booking = booking_stack[user].pop()
        available_properties.append(last_booking)
        print(f"{user} undid booking for {last_booking}.")
    else:
        print(f"{user} has no bookings to undo.")

def submit_application(user, property_name):
    if property_name in available_properties:
        application_queue.append((user, property_name))
        print(f"{user} submitted an application for {property_name}.")
    else:
        print(f"Sorry, {property_name} is not available.")

def process_next_application():
    if application_queue:
        user, property_name = application_queue.popleft()
        print(f"Processing application: {user} for {property_name}.")
    else:
        print("No applications to process.")

def show_available_properties():
    print("Available properties:", available_properties)

def show_user_bookings(user):
    print(f"{user}'s bookings:", booking_stack.get(user, []))

def menu():
    while True:
        choice = input("\n1. View properties\n2. Book\n3. Undo booking\n4. Submit application\n5. Process application\n6. Show bookings\n7. Exit\nChoose (1-7): ")
        
        if choice == "1": show_available_properties()
        elif choice == "2": book_property(input("Name: "), input("Property: "))
        elif choice == "3": undo_booking(input("Name: "))
        elif choice == "4": submit_application(input("Name: "), input("Property: "))
        elif choice == "5": process_next_application()
        elif choice == "6": show_user_bookings(input("Name: "))
        elif choice == "7": break
        else: print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()