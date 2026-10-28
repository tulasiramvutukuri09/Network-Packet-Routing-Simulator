
# main.py

import routing


while True:
    print("\n===== Network Packet Routing Simulator =====")
    print("1. View Network")
    print("2. Find Shortest Route")
    print("3. Simulate Connection Failure")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        routing.show_network()

    elif choice == "2":
        start = input("Enter starting computer (A-E): ").upper()
        end = input("Enter destination computer (A-E): ").upper()

        routing.find_route(start, end)

    elif choice == "3":
        first = input("Enter first computer (A-E): ").upper()
        second = input("Enter second computer (A-E): ").upper()

        routing.block_connection(first, second)

    elif choice == "4":
        print("Exiting simulator. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
