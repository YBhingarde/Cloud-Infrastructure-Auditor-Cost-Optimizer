def show_menu():
    print("\n================================")
    print("   Cloud Infrastructure Auditor")
    print("================================")
    print("1. Scan Resources")
    print("2. View Results")
    print("3. Generate Report")
    print("4. Help")
    print("5. Exit")


while True:
    show_menu()

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print("Scanning resources...")

    elif choice == "2":
        print("Showing scan results...")

    elif choice == "3":
        print("Generating report...")

    elif choice == "4":
        print("\nHelp:")
        print("1 - Scan AWS resources")
        print("2 - View previous scan results")
        print("3 - Generate reports")
        print("5 - Exit the application")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid option. Try again.")
