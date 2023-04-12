import os, shutil, datetime


def create_output_folder():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folders_array = ['Process_hawk', 'Networking_hawk', 'Logs_hawk', 'system_hawk', 'Users_hawk']
    destination_folder = f"MacHawk_Output_{current_time}"
    for folder in folders_array:
        try:
            shutil.copytree(folder, destination_folder + '/' + folder)
            print(f"Folder '{folder}' copied to '{destination_folder}' successfully!")
        except shutil.Error as e:
            print(f"An error occurred while copying folder '{folder}' to '{destination_folder}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred while copying folder '{folder}' to '{destination_folder}': {e}")
    for folder in folders_array:
        try:
            shutil.rmtree(folder)
            print(f"Folder '{folder}' deleted successfully!")
        except shutil.Error as e:
            print(f"An error occurred while deleting folder '{folder}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred while deleting folder '{folder}': {e}")