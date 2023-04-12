import subprocess, os

def hunt_for_all():
    create_output_dir()
    list_all_processes()


def create_output_dir():
    try:
        os.mkdir("Process_hawk")
    except FileExistsError:
        print("the directory already exist")
    except Exception as e:
        print(f"There was an error creating the Directory: {e}")


def list_all_processes():
    command = ['sudo', 'ps', '-axo user,pid,ppid,%cpu,%mem,start,time,command']
    result = subprocess.run(command, stdout=subprocess.PIPE)
    output = result.stdout.decode()
    file_path = os.path.join('Process_hawk', 'all_processes.txt')
    with open(file_path, 'w') as f:
        f.write(output)
    print(f"Netstat output saved to {file_path}")
