import os, shutil

def hunt_for_all():
    #create_output_dir()
    copy_directory()


def create_output_dir():
    try:
        os.mkdir("Logs_hawk")
    except FileExistsError:
        print("the directory already exist")
    except Exception as e:
        print(f"There was an error creating the Directory: {e}")


def copy_directory():
    src_dir = "/var/log/"
    dest_dir = "Logs_hawk/"
    try:
        shutil.copytree(src_dir, dest_dir)
        print(f"Directory '{src_dir}' copied to '{dest_dir}' successfully!")
    except shutil.Error as e:
        print(f"An error occurred while copying directory '{src_dir}' to '{dest_dir}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while copying directory '{src_dir}' to '{dest_dir}': {e}")