from commands.scan import scan
from commands.view_results import view_results
from commands.report import generate_report
from utils.logger import log_info

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
        view_results()

    elif choice == "3":

        generate_report()

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