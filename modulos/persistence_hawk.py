import subprocess, os, datetime, shutil


def hunt_for_all():
    create_output_dir()


def create_output_dir():
    try:
        os.mkdir("persistence_hawk")
    except FileExistsError:
        print("the directory already exist")
    except Exception as e:
        print(f"There was an error creating the Directory: {e}")


def copy_launchagents():
    src_dir = "/Library/LaunchAgents/"
    dest_dir = "persistence_hawk/LaunchAgents/"
    try:
        shutil.copytree(src_dir, dest_dir)
        print(f"Directory '{src_dir}' copied to '{dest_dir}' successfully!")
    except shutil.Error as e:
        print(f"An error occurred while copying directory '{src_dir}' to '{dest_dir}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while copying directory '{src_dir}' to '{dest_dir}': {e}")


def copy_launchdaemons():
    src_dir = "/Library/LaunchDaemons/"
    dest_dir = "persistence_hawk/LaunchDaemons/"
    try:
        shutil.copytree(src_dir, dest_dir)
        print(f"Directory '{src_dir}' copied to '{dest_dir}' successfully!")
    except shutil.Error as e:
        print(f"An error occurred while copying directory '{src_dir}' to '{dest_dir}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while copying directory '{src_dir}' to '{dest_dir}': {e}")