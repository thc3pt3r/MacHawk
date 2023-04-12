import subprocess, os

def hunt_for_all():
    create_output_dir()
    network_activity()
    list_file_with_open_connection()


def create_output_dir():
    try:
        os.mkdir("Networking_hawk")
    except FileExistsError:
        print("the directory already exist")
    except Exception as e:
        print(f"There was an error creating the Directory: {e}")


def network_activity():
    file_path = os.path.join('Networking_hawk', 'NETSTAT.txt')
    command = ['sudo', 'netstat', '-na']
    result = subprocess.run(command, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    with open(file_path, 'w') as f:
        f.write(output)
    print(f"Netstat output saved to {file_path}")


def list_file_with_open_connection():
    file_path = os.path.join('Networking_hawk', 'lsof_I.txt')
    command = ['sudo', 'lsof', '-i']
    result = subprocess.run(command, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    with open(file_path, 'w') as f:
        f.write(output)
    print(f"all files with an open IPv4, IPv6 or HP-UX X25 connection has been saved to {file_path}")