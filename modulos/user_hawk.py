import subprocess, os

def hunt_for_all():
    create_output_dir()
    previous_logged_user()
    active_logged_users()
    get_user_list()
    get_cleaned_user_list()


def create_output_dir():
    try:
        os.mkdir("Users_hawk")
    except FileExistsError:
        print("the directory already exist")
    except Exception as e:
        print(f"There was an error creating the Directory: {e}")


def previous_logged_user():
     command = ['sudo', 'last']
     file_path = os.path.join('Users_hawk', 'LAST.txt')
     result = subprocess.run(command, stdout=subprocess.PIPE)
     output = result.stdout.decode()
     with open(file_path, 'w') as f:
         f.write(output)
     print(f"Last command saved to {file_path}")


def active_logged_users():
    command = 'sudo w'
    file_path = os.path.join('Users_hawk', 'W_output.txt')
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    output = result.stdout.decode()
    with open(file_path, 'w') as f:
        f.write(output)
    print(f"W command saved to {file_path}")


def get_cleaned_user_list():
    command = 'sudo dscl . list /Users UniqueID | grep -v ^_'
    file_path = os.path.join('Users_hawk','no_systemAccount_List.txt')
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    output = result.stdout.decode()
    with open(file_path, 'w') as f:
        f.write(output)
    print(f'f"Cleaner User List saved to {file_path}"')


def get_user_list():
    command = 'sudo dscl . list /Users UniqueID'
    file_path = os.path.join('Users_hawk','Complete_user_List.txt')
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    output = result.stdout.decode()
    with open(file_path, 'w') as f:
        f.write(output)
    print(f'f"Complete User List saved to {file_path}"')