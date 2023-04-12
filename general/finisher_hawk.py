import os, shutil, datetime,tarfile


def create_output_folder():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folders_array = ['Process_hawk', 'Networking_hawk', 'Logs_hawk', 'system_hawk', 'Users_hawk', 'persistence_hawk']
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
    compress_output_files(destination_folder)
    try:
        shutil.rmtree(destination_folder)
    except shutil.Error as e:
        print(f"An error occurred while deleting folder '{destination_folder}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while deleting folder '{destination_folder}': {e}")


def compress_output_files(output_name):
    output_file = f"{output_name}.tar.gz"
    with tarfile.open(output_file, "w:gz") as tar:
        tar.add(output_name, arcname=os.path.basename(output_name))