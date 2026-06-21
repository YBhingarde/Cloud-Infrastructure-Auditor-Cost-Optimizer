from commands.scan import scan
from utils.logger import setup_logger

def show_menu():

    print("\n================================")
    print("   Cloud Infrastructure Auditor")
    print("================================")

    print("1. Scan Resources")
    print("2. View Results")
    print("3. Generate Report")
    print("4. Help")
    print("5. Exit")
    log_info("Application started")


while True:

    show_menu()

    choice = input("Choose an option (1-5): ")

    if choice == "1":

        scan()

    elif choice == "2":

        print("\n===== View Results =====")

        print("No scan results available.")

        print("Run Scan Resources first.")

    elif choice == "3":

        print("\n===== Generate Report =====")

        print("No report data available.")

        print("Run Scan Resources first.")

    elif choice == "4":

        print("\n===== Help =====")

        print("1 -> Scan AWS resources")

        print("2 -> View previous scan results")

        print("3 -> Generate report")

        print("5 -> Exit application")

    elif choice == "5":
        log_info("Application exited")

        print("Exiting application...")

        break

    else:

        print("Invalid option. Try again.")