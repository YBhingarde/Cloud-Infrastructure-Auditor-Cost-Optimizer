def show_menu():
    print("\n===== Cloud Auditor =====")
    print("1. Scan Resources")
    print("2. View Results")
    print("3. Export Report")
    print("4. Exit")


while True:
    show_menu()

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("Scanning resources...")

    elif choice == "2":
        print("Showing scan results...")

    elif choice == "3":
        print("Exporting report...")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid option. Try again.")