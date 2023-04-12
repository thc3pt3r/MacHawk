# This is a sample Python script.
from modulos import process_hawk as process_hawk, network_hawk as networking_hawk, user_hawk as users_hawk, \
    sytem_hawk as sys_hawk, log_hawk as logs_hawk
from general import finisher_hawk
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def show_menu():
    print("======= MacHawk - DTT CIR Triage =======")
    print("1. Run a complete IR Triage collection")
    print("2. Hunt for Processes")
    print("3. Hunt network activity")
    print("4. Hunt for User related outputs")
    print("5. exit")

    while True:
        try:
            choice = int(input("Please enter the number of choice: "))
            if choice < 1 or choice > 4:
                raise  ValueError
            break
        except ValueError:
            print("Invalid Input. Please select and option from the menu.")

    if choice == 1:
        process_hawk.hunt_for_all()
        networking_hawk.hunt_for_all()
        users_hawk.hunt_for_all()
        logs_hawk.hunt_for_all()
        sys_hawk.hunt_for_all()
        finisher_hawk.create_output_folder()
        # sys_hawk.sysdiagnose_hawk()
    elif choice == 2:
        print(process_hawk.list_process())
    elif choice == 3:
        print(networking_hawk.network_ativity())
    elif choice == 4:
        users_hawk.hunt_for_all()
    elif choice == 5:
        print("Exiting the menu.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    show_menu()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
