from modulos import process_hawk as process_hawk, network_hawk as networking_hawk, user_hawk as users_hawk, \
    sytem_hawk as sys_hawk, log_hawk as logs_hawk, browsing_hawk as browser_hawk, persistence_hawk as persist_hawk
from general import finisher_hawk
import sys


def show_menu():
    print("======= MacHawk - DTT CIR Triage =======")
    print("1. Run a complete IR Triage collection")
    print("2. exit")

    while True:
        try:
            choice = int(input("Please enter the number of choice: "))
            if choice < 1 or choice > 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid Input. Please select and option from the menu.")

    if choice == 1:
        process_hawk.hunt_for_all()
        networking_hawk.hunt_for_all()
        users_hawk.hunt_for_all()
        logs_hawk.hunt_for_all()
        sys_hawk.hunt_for_all()
        persist_hawk.hunt_for_all()
        finisher_hawk.create_output_folder()
        # sys_hawk.sysdiagnose_hawk()
    elif choice == 2:
        sys.exit(0)


if __name__ == '__main__':
    show_menu()
